
import pandas as pd


# The radiologist’s eyes were 28 inches away from the monitor
# Preparation of images. Preparation of images The 1,083 CXR images were converted from 
# DICOM format to .png format: normalized (0–255), resized and padded to 1920 × 1080 to fit 
# the radiologist’s computer’s monitor resolution (i.e., kept same aspect ratio)
class EyeGaze():

  def __init__(self, df : pd.DataFrame):
    """Initialises the EyeGaze class. 
    Args:
      df (pd.DataFrame): A pandas dataframe containing the gaze data.
          It must have the following columns:
          - timestamp (float): The timestamp of the gaze data
          - x (float): The x coordinate of the gaze data
          - y (float): The y coordinate of the gaze data
          - pupil_diameter (float): The pupil diameter of the gaze data"""
    self.df = df


  def clean_data(self):
    """Cleans the data"""
    pass


  def get_gaze_data(self):
    """Returns the gaze data"""
    return self.df

