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
	def __init__(self, dicom_id : str, study_id : str, report : str, dicom_path : str, annotation_lst : list):
  	
		# The Xray ID corresponds to the DICOM filename
		self.ID : str = dicom_id
		# each Xray is part of a study given by the studyID
		self.study_id : str = study_id
		# a radiologist must make a final report of the observations in the XRay
		# this report is from the hospital information system and can be used as a ground truth
		self.report : str = report

		patient_key = dicom_path.split("patient_")[1].split(os.sep)[0]
		# each Xray is stored in a DICOM file located in the DICOM_PATH
		self.dicom_path : str = dicom_path
		# each Xray is stored in a JPG file located in the JPG_PATH
		self.jpg_path : str = c.MIMIC_JPG_PATH(c.DATASET_PATH, patient_key,study_id, dicom_id)
		# getting the dimensions of the Xray image
		self.dims = self.dicom2array().shape

		# each Xray can have multiple annotations from different radiologists
		self.annotation_lst : list = annotation_lst

		# each Xray can have multiple eye gaze fixations from different radio logists
		self.eyegaze_fixations_path_lst = [c.EYE_GAZE_FIXATIONS_PATH(c.DATASET_PATH, patient_key)]
		self.eyegaze_raw_path_lst = [c.EYE_GAZE_RAW_PATH(c.DATASET_PATH, patient_key)]

	def dicom2array(self, voi_lut=True, fix_monochrome=True):
		# Use the pydicom library to read the dicom file
		dicom = pydicom.dcmread(self.dicom_path)
		
		# VOI LUT (if available by DICOM device) is used to 
		# transform raw DICOM data to "human-friendly" view
		if voi_lut:
				data = apply_voi_lut(dicom.pixel_array, dicom)
		else:
				data = dicom.pixel_array
				
		# The XRAY may look inverted
		#   - If we want to fix this we can
		if fix_monochrome and dicom.PhotometricInterpretation == "MONOCHROME1":
				data = np.amax(data) - data
		
		# Normalize the image array and return
		data = data - np.min(data)
		data = data / np.max(data)
		data = (data * 255).astype(np.uint8)
		return data

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

	# displays a DICOM Xray with the annotations
	def plot_annotations(self, label = False, figsize=(15, 20), fontsize=16):
  		
		# set figure size
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

		# for each annotation in the annotation list, plot it over the xray
		for annotation in self.annotation_lst:
			ax = annotation.plot_shape(ax, label, fontsize)

		# show the plot
		plt.tight_layout()
		plt.show()
		
	def show_report(self):
		print(self.report)

	def setReport(self, report : str):
		self.report = report

	def getDimensions(self):
		return self.dims

	def getReport(self):
		return self.report

	def getID(self):
		return self.ID

	def getStudyID(self):
		return self.study_id

	def getDICOMPath(self):
		return self.dicom_path

	def getJPGPath(self):
		return self.jpg_path
	
	def getEyegazeFixationsPath(self):
		return self.eyegaze_fixations_path

	def getEyegazeRawPath(self):
		return self.eyegaze_raw_path

