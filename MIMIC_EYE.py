"""
Author: Catarina Moreira
E-Mail: catarina.p.moreira@tecnico.ulisboa.pt
Date: January 5, 2023
"""

import pandas as pd
pd.set_option('display.max_columns', 500)

import numpy as np
import os
import sys
import shutil
import pickle as pkl
import matplotlib.pyplot as plt


from mimic.Patient import Patient
from mimic.Xray import Xray
from Constants import Constants as c
from data.groundtruth.BoundingBox import BoundingBox
from data.groundtruth.Ellipse import Ellipse

from util.mimic_data_processing import *


# Singleton class
# it is only instanciated once
class MIMIC_EYE():
  	
	# singleton instance
	_instance = None

	# starts a singleton instance
	# if the user tries to create more than one instance, it will raise an exception
	def __new__(cls):
		"""MIMIC_EYE Constructor"""
		if not cls._instance:
				cls._instance = super(MIMIC_EYE, cls).__new__(cls)
				return cls._instance
		else:
				raise Exception("[ERROR] MIMIC_EYE is a Singleton class and can only be instanciated ONCE!")
	
	# loads the previous state of the application
	# if it does not exist, it will create a new one by creating a new cache with the MIMIC_EYE database 
	def start(self):
		"""start function """
		if os.path.exists( c.CACHE_PATH ):
				self.load_state()
		else:
				self.initialize_mimic_eye()

	# saves the current state of the system, which is stored in the Constants.CACHE global variable
	def save_state(self):
		"""save_state function """
		pkl.dump( c.CACHE, open( c.CACHE_PATH, "wb" ) )

	# loads a previously saved pickle file containing the cache dictionary
	# the contents are stored in the Constants.CACHE global variable
	def load_state(self):
		"""load_state function """
		with open(c.CACHE_PATH, 'rb') as pickle_file:
			c.CACHE = pkl.load(pickle_file)

	
	def initialize_mimic_eye(self):
		"""initialize_mimic_eye function """
		PATIENTS_DIC = {}
		XRAY_TO_PATIENT = {}
		XRAY_TO_DIAGNOSIS = {}

		eye_gaze_sheet = os.path.join(c.DATASET_PATH, "spreadsheets", 'EyeGaze', "master_sheet_with_updated_stayId.csv")
		eye_gaze_df = pd.read_csv( eye_gaze_sheet )

		# extract all patient keys from EYE GAZE dataset
		patient_keys = eye_gaze_df['patient_id'].values.tolist()
		patient_keys = list(set(patient_keys))
		for patient_key in patient_keys:

				c.CACHE["EYE_GAZE"] = c.CACHE["EYE_GAZE"] + 1

				patient_dirs = os.listdir(c.PATIENT_PATH(c.DATASET_PATH, patient_key))
					
				# performs an inner join between the eye_gaze dataframe and the MIMIC core data on the patient_id key
				# this allows us to obtain all information about a patient
				# if there are multiple records of the patient (due to several visits to the hospital), we record the 
				# patient's information of his last visit to the hospital
				mimic_core = join_patients_mimic_core_data( patient_key, eye_gaze_df)

				# create a new Patient
				patient = Patient(mimic_core["patient_id"].tail(1).values[0], \
													mimic_core["gender_x"].tail(1).values[0], \
													mimic_core["language"].tail(1).values[0], \
													mimic_core["marital_status"].tail(1).values[0],\
													mimic_core["race"].tail(1).values[0], \
													mimic_core["anchor_age_x"].tail(1).values[0], \
													mimic_core["anchor_year"].tail(1).values[0], \
													mimic_core["dod"].tail(1).values[0], \
													mimic_core["anchor_year_group"].tail(1).values[0], {}, {}  )

				# get all CXR images associated to patient with patient_key
				xray_lst = []
				patient_df = eye_gaze_df[ eye_gaze_df[ "patient_id"] == patient_key ]
				for row in patient_df.itertuples():
					xray_id = row.dicom_id
					study_id = "s"+str(row.study_id)
					report = read_CXR_report( patient_key, study_id )
					diagnosis = get_diagnosis(row)
				
					XRAY_TO_DIAGNOSIS[xray_id] = diagnosis

					# a patient can have many imagaeology studies, and each study is composed of at least one XRay image
					# one xray is given by an image file, a textual report with all the findings and diagnosis
					# and a set of 
					xray_dicom_path = c.MIMIC_DICOM_PATH(c.DATASET_PATH, patient_key, study_id, xray_id)
				
					fixations_dict = {}
					transcripts_dict = {}
					gaze_dict = {}
					ell_annotation_dict = {}
					bbox_lst = []
					bboxes_df = pd.read_csv( c.EYE_GAZE_BBOX_PATH(c.DATASET_PATH, patient_key) )
					for bbox in bboxes_df.itertuples():
						bbox = BoundingBox(bbox.x1, bbox.x2, bbox.y1, bbox.y2, bbox.bbox_name)
						bbox_lst.append( bbox )

					cxr = Xray(xray_id, study_id, report, diagnosis, xray_dicom_path)
					cxr.setBboxList(bbox_lst)
					
					fixations_dict[study_id + "_" + xray_id] = c.EYE_GAZE_FIXATIONS_PATH(c.DATASET_PATH, patient_key)
					gaze_dict[study_id + "_" + xray_id] = c.EYE_GAZE_RAW_PATH(c.DATASET_PATH, patient_key)
					transcripts_dict[study_id + "_" + xray_id] = c.EYE_GAZE_TRANSCRIPTS_PATH(c.DATASET_PATH, patient_key, xray_id)

					if "REFLACX" in patient_dirs:

						metadata = pd.read_csv(c.REFLACX_METADATA(c.DATASET_PATH, patient_key))
						ref_row = metadata[ metadata["dicom_id"] == xray_id ]

						if len(ref_row) > 0:
							c.CACHE["REFLACX"] = c.CACHE["REFLACX"] + 1
							c.CACHE["OVERLAP"].append(patient_key)
			
						ell_annotation_dict = cxr.getAbnormalityDict()
						for ref in ref_row.itertuples():
						
							refl_id = ref.id
							
							temp = []
							if refl_id in ell_annotation_dict.keys():
								temp = ell_annotation_dict[refl_id]
							ellipse_annotations = pd.read_csv(c.REFLACX_ELLIPSE_PATH(c.DATASET_PATH, patient_key, refl_id))
							for ell in ellipse_annotations.itertuples():
								ell_labels = getLabelsFromREFLACX(ell, ellipse_annotations.columns.to_list())
								for ell_label in ell_labels:
									temp.append(Ellipse(ell.xmin, ell.xmax, ell.ymin, ell.ymax, ell_label, ell.certainty ))
							
							ell_annotation_dict[refl_id] = temp
							fixations_dict[refl_id + "_" + xray_id] = c.REFLACX_FIXATIONS_PATH(c.DATASET_PATH, patient_key, refl_id)
							gaze_dict[refl_id + "_" + xray_id] = c.REFLACX_RAW_PATH(c.DATASET_PATH, patient_key, refl_id)
							transcripts_dict[refl_id + "_" + xray_id] = c.REFLACX_TRANSCRIPTS_PATH(c.DATASET_PATH, patient_key, refl_id)

						
							cxr.setAbnormalityDict(ell_annotation_dict)


							# moving gaze files to the XAMI-MIMIC folder
							# source_gaze_file_path = c.REFLACX_GAZE_SOURCE_PATH(c.REFLACX_SOURCE, row.id)
							# destinatination_gaze_folder_path = c.REFLACX_RAW_PATH(c.DATASET_PATH, row.subject_id, row.id)
							# destinatination_gaze_folder_path.replace("gaze.csv", "")
							
							# print(f"Copying file from {source_gaze_file_path} to {destinatination_gaze_folder_path}")
							# shutil.copy(source_gaze_file_path, destinatination_gaze_folder_path )
						
					cxr.setFixationsDict(fixations_dict)
					cxr.setGazeDict(gaze_dict)
					cxr.setAudioTranscriptsDict(transcripts_dict)
					

					xray_lst.append( cxr )

					# get all fixations associated to the current xray
					# print(mimic_core["patient_id"].tail(1).values[0])
					# print(xray_id)
					# gaze_df = gaze_file[ gaze_file["DICOM_ID"] == xray_id ]
					# gaze_df.to_csv( cxr.getEyegazeRawPathList()[0], index=False )
					
					# print("saving EYE GAZE gaze file to " +  cxr.getEyegazeRawPathList()[0])


					XRAY_TO_PATIENT[xray_id] = patient

				# check if a patient key exists in PATIENTS_DIC
				if patient_key in PATIENTS_DIC:
					print(f"Patient {patient_key} already exists in PATIENTS_DIC. Processing DICOM ID {xray_id}")
					print(f"Current DICOM IDs")
					print(PATIENTS_DIC[patient_key].get_xray_ids())
					print("---------------------------------------------------------------------\n")
				
				patient.setXray_lst(xray_lst)
				PATIENTS_DIC[patient_key] = patient
				
		c.CACHE["PATIENTS"] = PATIENTS_DIC
		c.CACHE["XRAY_TO_PATIENT"] = XRAY_TO_PATIENT
		c.CACHE["XRAY_TO_DIAGNOSIS"] = XRAY_TO_DIAGNOSIS
		c.CACHE["OVERLAP"] = list(set(c.CACHE["OVERLAP"]))



	def load_eyegaze_dataset(self):
		"""load_eyegaze_dataset function """
		pass