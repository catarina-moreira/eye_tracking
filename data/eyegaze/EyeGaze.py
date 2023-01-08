
import pandas as pd

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
    super().__init__(df)


  def clean_data(self):
    """Cleans the data"""
    pass

  

  def get_gaze_data(self):
    """Returns the gaze data"""
    return self.df

