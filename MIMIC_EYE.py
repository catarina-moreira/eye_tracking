"""
Author: Catarina Moreira
E-Mail: catarina.p.moreira@tecnico.ulisboa.pt
Date: January 5, 2023
"""
import os
import pickle as pkl

from Constants import Constants as c


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
		c.CACHE = pkl.load(  c.CACHE_PATH )

	def initialize_mimic_eye(self):
		"""initialize_mimic_eye function """
		self.load_eyegaze_dataset()

	def load_eyegaze_dataset(self):
		"""load_eyegaze_dataset function """
		pass