import numpy as np
import matplotlib.pyplot as plt

import os
import pydicom
import pydicom.data
from pydicom.pixel_data_handlers.util import apply_voi_lut

from data.groundtruth.Annotation import Annotation
from data.groundtruth.BoundingBox import BoundingBox

from Constants import Constants as c

class Xray():
	def __init__(self, dicom_id : str, study_id : str, report : str, diagnosis :str, dicom_path : str):
  	
		# The Xray ID corresponds to the DICOM filename
		self.ID : str = dicom_id
		# each Xray is part of a study given by the studyID
		self.study_id : str = study_id
		# a radiologist must make a final report of the observations in the XRay
		# this report is from the hospital information system and can be used as a ground truth
		self.report : str = report
		# the diagnosis of the Xray
		self.diagnosis : str = diagnosis

		patient_key = dicom_path.split("patient_")[1].split(os.sep)[0]

		# each Xray is stored in a DICOM file located in the DICOM_PATH
		self.dicom_path : str = dicom_path
		# each Xray is stored in a JPG file located in the JPG_PATH
		self.jpg_path : str = c.MIMIC_JPG_PATH(c.DATASET_PATH, patient_key,study_id, dicom_id)
		# getting the dimensions of the Xray image
		try:
			self.dims = self.dicom2array().shape
		except:
			print(f"[WARNING] Patient {patient_key} does not contain DICOM file {self.dicom_path}")
			self.dims = (0,0)

		# each Xray has multiple Xray annotations of anatomical structures of the thorax (eye gaze only)
		self.bbox_lst : list = []

		# each Xray can have multiple fixations from different radiologists
		self.fixations_dict = {}
		self.gaze_dict = {}

		# each Xray may contain audio transcripts from different radiologists
		self.audio_transcripts_dict = {}

		# each Xray may contain several annotations of lesions
		self.abnormality_dict : dict = {}

	def getInfo(self):
		cxr_dict = {}
		cxr_dict["ID"] = self.ID
		cxr_dict["study_id"] = self.study_id
		cxr_dict["report"] = self.report
		cxr_dict["diagnosis"] = self.diagnosis
		cxr_dict["dicom_path"] = self.dicom_path
		cxr_dict["jpg_path"] = self.jpg_path
		cxr_dict["dims"] = self.dims
		cxr_dict["bbox_lst"] = self.bbox_lst
		cxr_dict["abnormality_dict"] = self.abnormality_dict
		cxr_dict["fixations_dict"] = self.fixations_dict
		cxr_dict["gaze_dict"] = self.gaze_dict
		cxr_dict["audio_transcripts_dict"] = self.audio_transcripts_dict
		return cxr_dict

	def normalize_image(self, data):
		data = data - np.min(data)
		data = data / np.max(data)
		data = (data * 255).astype(np.uint8)
		return data
  
	# converts a DICOM Xray to a numpy array
	def dicom2array(self, voi_lut=True, fix_monochrome=True):
		# Use the pydicom library to read the dicom file
		dicom = pydicom.dcmread(self.dicom_path)

		# VOI LUT (if available by DICOM device) is used to transform raw DICOM data to "human-friendly" view
		data =  apply_voi_lut(dicom.pixel_array, dicom) if voi_lut else dicom.pixel_array

		# The XRAY may look inverted
		if fix_monochrome and dicom.PhotometricInterpretation == "MONOCHROME1":
				data = np.amax(data) - data
		
		# Normalize the image array and return
		return self.normalize_image(data)

	# displays a DICOM Xray
	def show_dicom_xray(self):
		data = self.dicom2array()
		plt.imshow(data, cmap=plt.cm.bone)
		plt.show()

	# displays a JPG Xray
	def show_jpg_xray(self):
		data = plt.imread(self.jpg_path)
		plt.imshow(data, cmap=plt.cm.bone)
		plt.show()

	# plots a JPG Xray
	def xray_figure(self, figsize = (5,7)):
		plt.figure(figsize=(figsize))
		ax = plt.axes()

		# plot xray image
		img = plt.imread( self.jpg_path )
		ax.imshow(img, cmap=plt.cm.bone)

		# set the x and y limits of the plot
		plt.xlim([0, img.shape[1]])
		plt.ylim([0, img.shape[0]])

		# invert the y axis so that the origin is in the top left
		ax.invert_yaxis()
		return ax
  		

	def plot_abnormalities(self, figsize=(5, 7), label=True, fontsize=10, linewidth=2 ):
  	
		# plot the xray image
		ax = self.xray_figure(figsize = figsize)

		# invert the y axis so that the origin is in the top left
		readings = self.abnormality_dict.keys()
		print(readings)
		print(f"Number of radiologists annotating the image: {len(readings)}")
		for reading in readings:
			abnormalities = self.abnormality_dict[reading]
			for abnormality in abnormalities:
				abnormality.plot_shape(ax, label=label, fontsize=fontsize, linewidth=linewidth);
				ax.set_title(f"Radiologist {reading} annotations", fontsize=fontsize)


	# displays a DICOM Xray with the annotations
	def plot_bounding_boxess(self, annotation_labels = None, label = False, figsize=(5, 7), fontsize=16, linewidth=2):
  	
		# plot the xray image
		ax = self.xray_figure(figsize = figsize)

		# for each annotation in the annotation list, plot it over the xray
		for annotation in self.bbox_lst:
			# if no specific labels are given, plot all annotations
			if not annotation_labels:	
					ax = annotation.plot_shape(ax, label = label, fontsize=fontsize, linewidth=linewidth)
			else:
				# if specific labels are given, plot only those annotations
				if annotation.label.upper() in annotation_labels:
					ax = annotation.plot_shape(ax, label = label, fontsize=fontsize)
  				
		# show the plot
		plt.tight_layout()
		plt.show()
		
	def show_report(self):
		print(self.report)


	# getters and setters ----------------------------------------------
	def getReport(self):
		return self.report

	def setReport(self, report : str):
		self.report = report

	def getDimensions(self):
		return self.dims
	
	def setDimensions(self, new_dims):
		self.dims = new_dims

	def getID(self):
		return self.ID

	def setID(self, new_id):
		self.ID = new_id

	def getStudyID(self):
		return self.study_id

	def setStudyID(self, new_study_id):
		self.study_id = new_study_id

	def getDICOMPath(self):
		return self.dicom_path

	def setDICOMPath(self, new_dicom_path):
		self.dicom_path = new_dicom_path

	def getJPGPath(self):
		return self.jpg_path
	
	def setJPGPath(self, new_jpg_path):
		self.jpg_path = new_jpg_path

	def getDiagnosis(self):
		return self.diagnosis

	def setDiagnosis(self, new_diagnosis):
		self.diagnosis = new_diagnosis

	def getAbnormalityDict(self):
		return self.abnormality_dict

	def setAbnormalityDict(self, new_abnormality_dict : dict):
		self.abnormality_dict = new_abnormality_dict

	def getBboxList(self):
		return self.bbox_lst

	def setBboxList(self, new_bbox_lst):
		self.bbox_lst = new_bbox_lst

	def getFixationsDict(self):
		return self.fixations_dict
	
	def setFixationsDict(self, new_fixations_dict : dict):
		self.fixations_dict = new_fixations_dict
	
	def getGazeDict(self):
		return self.gaze_dict

	def setGazeDict(self, new_gaze_dict : dict):
		self.gaze_dict = new_gaze_dict
	
	def getAudioTranscriptsDict(self):
		return self.audio_transcripts_dict		
	
	def setAudioTranscriptsDict(self, new_audio_transcripts_dict : dict):
		self.audio_transcripts_dict = new_audio_transcripts_dict

	
	


	


