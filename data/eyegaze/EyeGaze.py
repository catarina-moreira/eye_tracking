
import pandas as pd
import os
from Constants import Constants as c

# The radiologist’s eyes were 28 inches away from the monitor
# Preparation of images. Preparation of images The 1,083 CXR images were converted from 
# DICOM format to .png format: normalized (0–255), resized and padded to 1920 × 1080 to fit 
# the radiologist’s computer’s monitor resolution (i.e., kept same aspect ratio)
class EyeGaze():


  DESCRIPTION = {
    "DICOM_ID" : "DICOM_ID from the original MIMIC dataset",
    "CNT" : "The counter data variable is incremented by 1 for each data record sent by the server. Useful to determine if any data packets are missed by the client",
    "Time (in secs)" : "The time elapsed in seconds since the last system initialization or callibration. The time stamp is recorded at the end of the transmission of the image from camera to computer. USeful for synchronization and to determine if the server computer is processing the images at the full frame rate, For a 60Hz camera, the TIME value should increment by 1/60 seconds.",
    "TIMETICK(f=10000000)" : "This is a 64-bit integer which indicates the number of CPU time ticks for high precision synchronization with other dta collected on the same CPU",
    "FPOGX" : "The X-coordinate of the fixation POG (point of gaze) as a fraction of the screen size. (0,0) is top left, (0.5, 0.5) is the screen center and (1.0, 1.0) is the bottom right",
    "FPOGY" : "The Y-coordinate of the fixation POG (point of gaze) as a fraction of the screen size. (0,0) is top left, (0.5, 0.5) is the screen center and (1.0, 1.0) is the bottom right",
    "FPOGS" : "The starting time of the fixation POG in seconds since the system initialitization or calibration",
    "FPOGD" : "The duration of the fixation POG in seconds",
    "FPOGID" : "The fixation POG ID. This is a unique ID for each fixation POG. It is incremented by 1 for each new fixation POG",
    "FPOGV" : "The valid flag with value 1 (TRUE) if the fixation POG data is valid, and 0 (FALSE) if it is not. FPOGV valid is TRUE ONLY when either one, or both, of the eyes are detected AND a fixation is detected. FPOGV is FALSE all other times, for example when the participant blinks, when there is no face in the fiel of view, when the eye move to the next fixation (i.e. a saccade)",
    "BPOGX" : "The X-coordinate of the blink POG (point of gaze) as a fraction of the screen size.",
    "BPOGY" : "The Y-coordinate of the blink POG (point of gaze) as a fraction of the screen size.",
    "BPOGV" : "The valid flag with value of 1 if the data is valid, and 0 if it is not",
    "LPCX"  : "The X-coordinate of the left eye pupil in the camera image as a fraction of the camera image size",
    "LPCY"  : "The Y-coordinate of the left eye pupil in the camera image as a fraction of the camera image size",
    "LPD"   : "The diameter of the left eye pupil in pixels",
    "LPS"   : "The scale factor of the left eye pupil (unitless). Value equals 1 at calibration depth, is less than 1 when user is closer to the eye tracker  and greater than 1 when user is further away",
    "LPV"   : "The valid flag with value of 1 if the data is valid, and 0 if it is not",
    "RPCX"  : "The X-coordinate of the right eye pupil in the camera image as a fraction of the camera image size",
    "RPCY"  : "The Y-coordinate of the right eye pupil in the camera image as a fraction of the camera image size",
    "RPD"   : "The diameter of the right eye pupil in pixels",
    "RPS"   : "The scale factor of the right eye pupil (unitless). Value equals 1 at calibration depth, is less than 1 when user is closer to the eye tracker  and greater than 1 when user is further away",
    "RPV"   : "The valid flag with value of 1 if the data is valid, and 0 if it is not",
    "BKID"  : "Each blink is assigned a unique ID. This ID is incremented by 1 for each new blink. THE BKID value equals 0 for every record where no blink has been recorded",
    "BKDUR" : "The duration of the preceeding blink in seconds",
    "BKPMIN": "The number of blinks in the previous 60 second period of time",
    "LPMM"  : "The diameter of the left eye pupil in milimeters",
    "LPMMV" : "The valid flag with value of 1 if the data is valid, and 0 if it is not",
    "RPMM"  : "The diameter of the right eye pupil in milimeters",
    "RPMMV" : "The valid flag with value of 1 if the data is valid, and 0 if it is not",
    "SACCADE_MAG" : "The magnitude of the saccade calculated as the distance between each fixation (in pixels)",
    "SACCADE_DIR" : "The direction or angle between each fixation (in degrees from horizontal)",
    "X_ORGINAL" : "The X-coordinate of the fixation in original DICOM image",
    "Y_ORIGINAL" : "The Y-coordinate of the fixation in original DICOM image" 
  }

  def __init__(self, filepath: str):
    print("Loading gaze and fixations data from EYE GAZE ...")
    self.filepath : str = filepath
    self.df_gaze : pd.DataFrame = pd.read_csv(os.path.join(filepath, "gaze.csv"))
    self.df_fixations : pd.DataFrame = pd.read_csv(os.path.join(filepath, "fixations.csv"))
    print("done!\n")

  def clean_data(self):
    """Cleans the data"""
    # delete all gaze data and fixations data that fall outside of the image
    dicom_id = self.df_gaze["DICOM_ID"].iloc[0]
    cxr = c.CACHE["DICOM_TO_XRAY"][dicom_id]
    img_dims = cxr.getDimensions()
    self.df_gaze = self.df_gaze[ (self.df_gaze["X_ORIGINAL"] >= 0) and (self.df_gaze["Y_ORIGINAL"] >= 0) ]
    self.df_gaze = self.df_gaze[ (self.df_gaze["X_ORIGINAL"] <= img_dims[0]) and (self.df_gaze["Y_ORIGINAL"] <= img_dims[1]) ]

    self.df_fixations = self.df_fixations[ (self.df_fixations["X_ORIGINAL"] >= 0) and (self.df_fixations["Y_ORIGINAL"] >= 0) ]
    self.df_gaze = self.df_fixations[ (self.df_fixations["X_ORIGINAL"] <= img_dims[0]) and (self.df_fixations["Y_ORIGINAL"] <= img_dims[1]) ]


  def process_time(self):
    pass


  def get_gaze_data(self):
    """Returns the gaze data"""
    return self.df_gaze

  def get_fixations_data(self):
    """Returns the fixations data"""
    return self.df_fixations

  def set_gaze_data(self, df: pd.DataFrame):
    """Sets the gaze data"""
    self.df_gaze = df

  def set_fixations_data(self, df: pd.DataFrame):
    """Sets the fixations data"""
    self.df_fixations = df

  def get_gaze_data_by_time(self, start_time: float, end_time: float):
    """Returns the gaze data between the start_time and end_time"""
    return self.df_gaze[ (self.df_gaze["TIME"] >= start_time) and (self.df_gaze["TIME"] <= end_time) ]

  def get_fixations_data_by_time(self, start_time: float, end_time: float):
    """Returns the fixations data between the start_time and end_time"""
    return self.df_fixations[ (self.df_fixations["TIME"] >= start_time) and (self.df_fixations["TIME"] <= end_time) ]
