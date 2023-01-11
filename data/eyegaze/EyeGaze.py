
import pandas as pd


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
    ""


  }

  def __init__(self, df : pd.DataFrame):
    self.df = df


  def clean_data(self):
    """Cleans the data"""
    pass


  def get_gaze_data(self):
    """Returns the gaze data"""
    return self.df

 
