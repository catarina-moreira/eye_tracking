from mimic.Transfer import Transfer
from mimic.EDStay import EDStay
from typing import List

class Admission(object):

	def __init__(self):
		# Unique ID representing a single patient's admission to the hospital
		self.__hadmin_id : str = None
		
		self.__tranfers_list : Transfer = None
		# provides the date and time the patient was admitted to the hospital
		self.__edstay_list : EDStay = None
		
		self.__admittime : str = None

		# provides the date and time the patient was discharged from the hospital
		self.__dischtime : str = None
		
		# If applicable, deathtime provides the time of in-hospital death for the patient. 
		# Note that deathtime is only present if the patient died in-hospital, and is almost always the same as the patient’s dischtime
		self.__deathtime : str = None
		
		# is useful for classifying the urgency of the admission. 
		# There are 9 possibilities: ‘AMBULATORY OBSERVATION’, ‘DIRECT EMER.’, 
		# ‘DIRECT OBSERVATION’, ‘ELECTIVE’, ‘EU OBSERVATION’, ‘EW EMER.’, ‘OBSERVATION ADMIT’, ‘SURGICAL SAME DAY ADMISSION’, ‘URGENT’.
		self.__admission_type : str = None
		
		# provides information about the location of the patient prior to arriving at the hospital. Note that as the emergency room 
		# is technically a clinic, patients who are admitted via the emergency room usually have it as their admission location.
		self.__admission_location : str = None

		# It is the disposition of the patient after they are discharged from the hospital."""
		self.__discharge_location : str = None

		self.__insurance : str = None
		self.__edregtime : str = None
		self.__edouttime : str = None
		# This is a binary flag which indicates whether the patient died within the given hospitalization. 
		# 1 indicates death in the hospital, and 0 indicates survival to hospital discharge.
		self.__hospital_expire_flag : int = None
		

	## GETTERS AND SETTERS
	def setEdstay_list(self, edstay_list : EDStay):
		self.__edstay_list = edstay_list

	def getEdstay_list(self) -> EDStay:
		return self.__edstay_list

	def setAdmittime(self, admittime : str):
		self.__admittime = admittime

	def getAdmittime(self) -> str:
		return self.__admittime

	def setDischtime(self, dischtime : str):
		self.__dischtime = dischtime

	def getDischtime(self) -> str:
		return self.__dischtime

	def setDeathtime(self, deathtime : str):
		self.__deathtime = deathtime

	def getDeathtime(self) -> str:
		return self.__deathtime

	def setAdmission_type(self, admission_type : str):
		self.__admission_type = admission_type

	def getAdmission_type(self) -> str:
		return self.__admission_type

	def setAdmission_location(self, admission_location : str):
		self.__admission_location = admission_location

	def getAdmission_location(self) -> str:
		return self.__admission_location

	def setDischarge_location(self, discharge_location : str):
		self.__discharge_location = discharge_location

	def getDischarge_location(self) -> str:
		return self.__discharge_location

	def setInsurance(self, insurance : str):
		self.__insurance = insurance

	def getInsurance(self) -> str:
		return self.__insurance

	def setEdregtime(self, edregtime : str):
		self.__edregtime = edregtime

	def getEdregtime(self) -> str:
		return self.__edregtime

	def setEdouttime(self, edouttime : str):
		self.__edouttime = edouttime

	def getEdouttime(self) -> str:
		return self.__edouttime

	def setHospital_expire_flag(self, hospital_expire_flag : int):
		self.__hospital_expire_flag = hospital_expire_flag

	def getHospital_expire_flag(self) -> int:
		return self.__hospital_expire_flag

	def getHadmin_id(self) -> str:
			return self.__hadmin_id

	def getHospital_expire_flag(self) -> int:
			return self.__hospital_expire_flag

	def setTranfers_list(self, tranfers_list : Transfer):
			self.__tranfers_list = tranfers_list
		
	def getTranfers_list(self) -> Transfer:
			return self.__tranfers_list
  	

		
	

