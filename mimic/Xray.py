import numpy as np
import matplotlib.pyplot as plt

import pydicom
import pydicom.data
from pydicom.pixel_data_handlers.util import apply_voi_lut

from data.eyegaze import BoundingBox
from Constants import Constants as c

class Xray():
	def __init__(self, dicom_id : str, study_id : str, report : str, dicom_path : str, jpg_path : str, bbox : list):
  	
		# The Xray ID corresponds to the DICOM filename
		self.ID : str = dicom_id
		self.study_id : str = study_id
		self.report : str = report
		self.dicom_path : str = dicom_path
		self.jpg_path : str = jpg_path
		self.bbox : list = bbox
		img = self.dicom2array()
		self.dims : int = img.shape

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

	def show_report(self, ID : str):
		pass

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