
import pandas as pd


# Heat maps: These are graphical representations of the distribution of gaze data over a particular area,
# They can reveal which areas of the interface are most frequently viewed, and which are neglected.
def get_heatmap_data(self, fixations : pd.DataFrame, saccades : pd.DataFrame):
  """Returns a dict containing the heatmap data"""
  # implement this function



# AOI analysis: AOI stands for "Area of Interest." This type of analysis identifies specific regions of 
# an interface that are most relevant to the task at hand, and then determines how often the user looks at them.
# It can reveal which AOIs are most frequently viewed, and which are overlooked.

def get_aoi_data(self, aoi : str, fixations : pd.DataFrame, saccades : pd.DataFrame):
  """Returns a dict containing the AOI data for the provided AOI"""
  pass
  
def get_aoi_fixations(self, aoi : str, fixations : pd.DataFrame):
  """Returns a dict containing the AOI fixation data for the provided AOI"""
  pass

def get_aoi_saccades(self, aoi : str, saccades : pd.DataFrame):
  """Returns a dict containing the AOI saccade data for the provided AOI"""
  pass

def get_aoi_dwell_time(self, aoi : str, fixations : pd.DataFrame):
  """Returns a dict containing the AOI dwell time data for the provided AOI"""
  pass

def get_aoi_fixation_count(self, aoi : str, fixations : pd.DataFrame):
  """Returns a dict containing the AOI fixation count data for the provided AOI"""
  pass

def get_aoi_saccade_count(self, aoi : str, saccades : pd.DataFrame):
  """Returns a dict containing the AOI saccade count data for the provided AOI"""
  pass

def get_aoi_fixation_duration(self, aoi : str, fixations : pd.DataFrame):
  """Returns a dict containing the AOI fixation duration data for the provided AOI"""
  pass

def get_aoi_saccade_duration(self, aoi : str, saccades : pd.DataFrame):
  """Returns a dict containing the AOI saccade duration data for the provided AOI"""
  pass

def get_aoi_fixation_distance(self, aoi : str, fixations : pd.DataFrame):
  """Returns a dict containing the AOI fixation distance data for the provided AOI"""
  pass

def get_aoi_saccade_distance(self, aoi : str, saccades : pd.DataFrame):
  """Returns a dict containing the AOI saccade distance data for the provided AOI"""
  pass

def get_aoi_fixation_velocity(self, aoi : str, fixations : pd.DataFrame):
  """Returns a dict containing the AOI fixation velocity data for the provided AOI"""
  pass

def get_aoi_saccade_velocity(self, aoi : str, saccades : pd.DataFrame):
  """Returns a dict containing the AOI saccade velocity data for the provided AOI"""
  pass

def get_aoi_fixation_acceleration(self, aoi : str, fixations : pd.DataFrame):
  """Returns a dict containing the AOI fixation acceleration data for the provided AOI"""
  pass

def get_aoi_saccade_acceleration(self, aoi : str, saccades : pd.DataFrame):
  """Returns a dict containing the AOI saccade acceleration data for the provided AOI"""
  pass

def get_aoi_fixation_pursuit(self, aoi : str, fixations : pd.DataFrame):
  """Returns a dict containing the AOI fixation pursuit data for the provided AOI"""
  pass

def get_aoi_saccade_pursuit(self, aoi : str, saccades : pd.DataFrame):
  """Returns a dict containing the AOI saccade pursuit data for the provided AOI"""
  pass



