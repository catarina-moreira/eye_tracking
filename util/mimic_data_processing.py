

import pandas as pd

from Constants import Constants as c

def join_patients_mimic_core_data(patient_id : str, eye_gaze_df : pd.DataFrame):
  """join_patients_mimic_core_data function """

  mimic_core = pd.read_csv( c.MIMIC_CORE_PATH(c.DATASET_PATH, patient_id, c.MIMIC_CORE_TABLES[0]) )
  for core_table in c.MIMIC_CORE_TABLES[1:]:

    try:
      mimic_core_tmp = pd.read_csv( c.MIMIC_CORE_PATH(c.DATASET_PATH, patient_id, core_table) )
      mimic_core = mimic_core.merge(mimic_core_tmp, on="subject_id")
    except:
      print(f"[WARNING] Patient {patient_id} does not contain database file {core_table}")
      continue
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
