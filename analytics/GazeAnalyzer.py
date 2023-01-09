# original code from
# __author__ = "Edwin Dalmaijer"
# __url__ = "https://github.com/esdalmaijer/PyGazeAnalyser/blob/master/pygazeanalyser/gazeplotter.py"

from typing import List

# native
import os
import pandas as pd
# external
import numpy
import matplotlib
from matplotlib import pyplot, image
import matplotlib.pyplot as plt

from Constants import Constants as c

class GazeAnalyzer():
  	
	def __init__(self):
		"""GazeAnalyzer Constructor"""
		pass
	
	def draw_raw(self, x : float, y : float, imagefile : str = None, savefilename : str =None):
  
		# image
		img = plt.imread( imagefile  )
		dispsize = img.transpose(1,0).shape

		fig, ax = self.draw_display(dispsize, imagefile=imagefile)

		# plot raw data points
		ax.plot(x, y, 'o', color=c.COLORS['chocolate'][0], markeredgecolor=c.COLORS['chocolate'][2], markersize=10)

		# invert the y axis, as (0,0) is top left on a display
		ax.invert_yaxis()

		# save the figure if a file name was provided
		if savefilename != None:
			fig.savefig(savefilename)

		return fig

	def draw_raw_no_processing(elf, x : float, y : float, figsize = (10,15), imagefile : str = None, savefilename : str =None):
  		
			plt.figure(figsize=figsize)
			img = plt.imread( imagefile  )
			implot = plt.imshow(img, cmap=plt.cm.bone)
			plt.plot(x, y, 'o', color=c.COLORS['chocolate'][0], markeredgecolor=c.COLORS['chocolate'][2], markersize=10)
			plt.tight_layout()
			plt.show()

			
	def draw_fixations(self, fixations : pd.DataFrame, dispsize : list = [1920, 1080], imagefile : str = None, durationsize : float = True, durationcolour : str = True, alpha : float = 0.5, savefilename : str = None):
		pass

	def draw_scanpath(self, fixations : pd.DataFrame, saccades : pd.DataFrame, dispsize : str, imagefile : str = None, alpha : float = 0.5, savefilename : str = None):
		"""Draws a scanpath: a series of arrows between numbered fixations, optionally drawn over an image"""
		pass

	def draw_heatmap(self, fixations : pd.DataFrame, dispsize : int, imagefile : None, durationweight : float = True, alpha : float = 0.5, savefilename : str = None ):
		"""Draws a heatmap of the provided fixations, optionally drawn over an image, and optionally allocating more weight to fixations with a higher duration"""
		pass

	def draw_display(self, dispsize : list = [1080, 1920], imagefile : str = None, dpi = 100):
  
		# construct screen (black background)
		_, ext = os.path.splitext(imagefile)
		ext = ext.lower()
		data_type = 'float32' if ext == '.png' else 'uint8'
		screen = numpy.zeros((dispsize[1],dispsize[0]), dtype=data_type)
		
		# if an image location has been passed, draw the image
		if imagefile != None:
			
			# load image
			img = image.imread(imagefile)

			# width and height of the image
			w, h = len(img[0]), len(img)

			# x and y position of the image on the display
			x = int(dispsize[0]/2 - w/2)
			y = int(dispsize[1]/2 - h/2)

			# draw the image on the screen
			screen[y:y+h,x:x+w] += img
		
		# determine the figure size in inches
		figsize = (dispsize[0]/dpi, dispsize[1]/dpi)
		# create a figure
		fig = pyplot.figure(figsize=figsize, dpi=dpi, frameon=False)
		ax = pyplot.Axes(fig, [0,0,1,1])
		ax.set_axis_off()
		fig.add_axes(ax)
		# plot display
		ax.axis([0,dispsize[0],0,dispsize[1]])
		ax.imshow(screen, cmap=plt.cm.bone)#, origin='upper')
		
		return fig, ax

	def gaussian(self, x : int, sx : float, y : int, sy : float):
		"""Returns an array of numpy arrays (a matrix) containing values between 1 and 0 in a 2D Gaussian distribution"""
		pass

	def parse_fixations(self, fixations : pd.DataFrame):
		"""Returns all relevant data from a list of fixation ending events:
		a dict with three keys: 'x', 'y', and 'dur' (each contain a numpy array) for the x and y coordinates and duration of each fixation"""
		pass

