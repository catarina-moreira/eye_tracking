
from mimic.Xray import Xray
from mimic.Annotation import Annotation

class XrayStudy( ):
  	
	def __init__(self, studyId : str, Xray_lst, annotation_lst : list):
		self.ID : str = studyId
		self.Xray_lst : Xray = Xray_lst


	def add_xray(self, new_xray : Xray):
		self.Xray_lst.append( new_xray )


	def remove_xray(self, xray : Xray):
		self.Xray_lst.remove( xray )


	def getID(self):
		return self.ID

	def setXray_lst(self, xray_lst : Xray):
		self.Xray_lst = xray_lst

	def getXray_lst(self):
		
		return self.Xray_lst
