import numpy as np
import matplotlib.pyplot as plt

import pydicom
import pydicom.data
from pydicom.pixel_data_handlers.util import apply_voi_lut

from mimic.Annotation import Annotation

from data.eyegaze import BoundingBox

from Constants import Constants as c

class Xray():
	def __init__(self, dicom_id : str, study_id : str, report : str, dicom_path : str, jpg_path : str, annotation_lst : list):
  	
		# The Xray ID corresponds to the DICOM filename
		self.ID : str = dicom_id
		self.study_id : str = study_id
		self.report : str = report
		self.dicom_path : str = dicom_path
		self.jpg_path : str = jpg_path
		self.annotation_lst : list = annotation_lst
		img = self.dicom2array()
		self.dims = img.shape

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

	def show_dicom_xray(self):
		data = self.dicom2array()
		plt.imshow(data, cmap=plt.cm.bone)
		plt.show()

	def show_jpg_xray(self):
		data = plt.imread(self.jpg_path)
		plt.imshow(data, cmap=plt.cm.bone)
		plt.show()

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

	def setPath(self, path : str):
		self.path = path

	def getPath(self):
		return self.path

	def getID(self):
		return self.ID

	def getStudyID(self):
		return self.study_id

	def getDICOMPath(self):
		return self.dicom_path

	def getJPGPath(self):
		return self.jpg_path