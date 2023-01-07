from typing import List

import pandas as pd

class GazeAnalyzer():
	def draw_raw(self, x : float, y : float, dispsize : float, imagefile : str = None, savefilename : str = None):
		"""Draws the raw x and y data"""
		pass

	def draw_fixations(self, fixations : pd.DataFrame, dispsize : int, imagefile : str = None, durationsize : float = True, durationcolour : str = True, alpha : float = 0.5, savefilename : str = None):
		pass

	def draw_scanpath(self, fixations : pd.DataFrame, saccades : pd.DataFrame, dispsize : str, imagefile : str = None, alpha : float = 0.5, savefilename : str = None):
		"""Draws a scanpath: a series of arrows between numbered fixations, optionally drawn over an image"""
		pass

	def draw_heatmap(self, fixations : pd.DataFrame, dispsize : int, imagefile : None, durationweight : float = True, alpha : float = 0.5, savefilename : str = None ):
		"""Draws a heatmap of the provided fixations, optionally drawn over an image, and optionally allocating more weight to fixations with a higher duration"""
		pass

	def draw_display(self, dispsize : int, imagesize : str = None):
		"""returns matplotlib.pyplot Figure and its axes: field of zeros with a size of dispsize, and an image drawn onto it if an imagefile was passed"""
		pass

	def gaussian(self, x : int, sx : float, y : int, sy : float):
		"""Returns an array of numpy arrays (a matrix) containing values between 1 and 0 in a 2D Gaussian distribution"""
		pass

	def parse_fixations(self, fixations : pd.DataFrame):
		"""Returns all relevant data from a list of fixation ending events:
		a dict with three keys: 'x', 'y', and 'dur' (each contain a numpy array) for the x and y coordinates and duration of each fixation"""
		pass

