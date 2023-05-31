import pandas as pd

from data.EyeGaze import EyeGaze
from data.REFLACX import REFLACX

from analytics.GazeAnalyzer import GazeAnalyzer

class GazeIntegrator(GazeAnalyzer):

  def __init__(self, eyegaze : EyeGaze = None, reflacx : REFLACX = None):
    """Initialises the GazeIntegrator class.
    Args:
      eyegaze (EyeGaze): An instance of the EyeGaze class
      reflacx (REFLACX): An instance of the REFLACX class"""
    super().__init__
    
    self.eyegaze = eyegaze
    self.reflacx = reflacx

  def standardiseEyeGaze(self):
    """Integrates the gaze data"""
    pass

  def standardiseReflacx(self):
    """Integrates the gaze data"""
  pass

  def get_integrated_data(self):
    """Returns the integrated data"""
    pass
