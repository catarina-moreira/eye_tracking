

import pandas as pd
import numpy as np

from Constants import Constants as c

def join_patients_mimic_core_data(patient_id : str, eye_gaze_df : pd.DataFrame):
  """join_patients_mimic_core_data function """

  mimic_core = pd.read_csv( c.MIMIC_CORE_PATH(c.DATASET_PATH, patient_id, c.MIMIC_CORE_TABLES[0]) )
  for core_table in c.MIMIC_CORE_TABLES[1:]:

    try:
      mimic_core_tmp = pd.read_csv( c.MIMIC_CORE_PATH(c.DATASET_PATH, patient_id, core_table) )
    except:
      print(f"[WARNING] Patient {patient_id} does not contain database file {core_table}")
      print("Adding admissions file with empty columns")

      admin_cols = ["Unnamed: 0","subject_id","hadm_id","admittime","dischtime","deathtime","admission_type","admission_location","discharge_location","insurance","language","marital_status","race","edregtime","edouttime","hospital_expire_flag"]
      mimic_core_tmp = pd.DataFrame(-1*np.ones((1,len(admin_cols))),columns=admin_cols)
      mimic_core_tmp.loc[0,"subject_id"] = patient_id 
      mimic_core["subject_id"] = mimic_core["subject_id"].astype(int)
      mimic_core_tmp.to_csv(c.MIMIC_CORE_PATH(c.DATASET_PATH, patient_id, core_table), index=False)
    
    try:
      mimic_core = mimic_core.merge(mimic_core_tmp, on="subject_id")
    except:
      print("This line raised an error")
      print(mimic_core_tmp)

  mimic_core.rename(columns = {'subject_id':'patient_id'}, inplace = True)
  return mimic_core.merge(eye_gaze_df, on="patient_id")


def read_CXR_report(patient_key : str, study_id : str):
  """read_CXR_report function """
  report = ""
  with open(c.MIMIC_CXR_REPORT(c.DATASET_PATH, patient_key, study_id)) as f:
      while True:
          line = f.readline()
          if not line:
              break
          report += line.strip()+"\n"
  return report

# check which column ("Normal", "CHF" or "Pneumonia") has a 1 in the eye_gaze_df dataframe
def get_diagnosis(row):
    diagnosis = "Normal"
    if row.CHF == 1:
        diagnosis = "CHF"
    if row.pneumonia == 1:
        diagnosis = "Pneumonia"
    return diagnosis

def getLabelsFromREFLACX(df, abnormalities):
  
  abnormalities_lst = []
  for abn in range(0,len(abnormalities)):
    if str(df[abn]) == "True":
      abnormalities_lst.append(abnormalities[abn])
  return abnormalities_lst

