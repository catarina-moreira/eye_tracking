
import matplotlib
import matplotlib.pyplot as plt
import os

class Constants():

	# only change this path!
	# main path where the dataset is stored
	DATASET_PATH = os.path.join("/", "Volumes", "SD_DISK", "XAMI-MIMICv2.0", "")
	REFLACX_SOURCE = os.path.join("/", "Volumes", "SD_DISK", "REFLACX", "")

	# patient main path
	PATIENT_PATH = lambda dataset_path, patient_id: os.path.join(dataset_path, "patient_" + str(patient_id))

	# mimic core path
	MIMIC_CORE_TABLES = ["patients", "admissions", "transfers"]
	MIMIC_CORE_PATH = lambda dataset_path, patient_id, table: os.path.join(dataset_path, "patient_" + str(patient_id), "Core",  table +".csv" )

	# mimic ed paths
	MIMIC_ED_TABLES = ["diagnosis", "edstays", "medrecon", "pyxis", "triage"]
	MIMIC_ED_PATH = lambda dataset_path, patient_id, table: os.path.join(dataset_path, "patient_" + str(patient_id), "ED",  table + ".csv" )

	# mimic cxr paths
	MIMIC_DICOM_PATH = lambda dataset_path, patient_id, study_id, dicom_id: os.path.join(dataset_path, "patient_" + str(patient_id), "CXR-DICOM", study_id, dicom_id + ".dcm")
	MIMIC_JPG_PATH   = lambda dataset_path, patient_id, study_id, dicom_id: os.path.join(dataset_path, "patient_" + str(patient_id), "CXR-JPG",   study_id, dicom_id + ".jpg")
	MIMIC_CXR_REPORT = lambda dataset_path, patient_id, study_id: os.path.join(dataset_path, "patient_" + str(patient_id), "CXR-DICOM", study_id + ".txt")

	# mimic cxr neg bio annotations
	MIMIC_NEG_BIO_PATH = lambda dataset_path, patient_id: os.path.join(dataset_path, "patient_" + str(patient_id), "CXR-JPG", "cxr_negbio.csv" )

	# mimic cxr chexpert annotations
	MIMIC_CHEXPERT_PATH = lambda dataset_path, patient_id: os.path.join(dataset_path, "patient_" + str(patient_id), "CXR-JPG", "cxr_chexpert.csv" )

	# mimic cxr metadata
	MIMIC_CHEXPERT_PATH = lambda dataset_path, patient_id: os.path.join(dataset_path, "patient_" + str(patient_id), "CXR-JPG", "cxr_meta.csv" )

	# eye gaze bounding boxes
	EYE_GAZE_BBOX_PATH = lambda dataset_path, patient_id : os.path.join(dataset_path, "patient_" + str(patient_id), "EyeGaze", "bounding_boxes.csv" )
	EYE_GAZE_FIXATIONS_PATH = lambda dataset_path, patient_id : os.path.join(dataset_path, "patient_" + str(patient_id), "EyeGaze", "fixations.csv" )
	EYE_GAZE_RAW_PATH = lambda dataset_path, patient_id : os.path.join(dataset_path, "patient_" + str(patient_id), "EyeGaze", "gaze.csv" )

	# eye gaze transcripts
	EYE_GAZE_TRANSCRIPTS_PATH = lambda dataset_path, patient_id, dicom_id : os.path.join(dataset_path, "patient_" + str(patient_id), "EyeGaze", "audio_segmentation_transcripts", dicom_id, "transcript.json" )
	
	# eye gaze segmentations
	SEGMENTATION_LIST = ["aortic_knob", "left_lung", "mediastanum", 'right_lung']
	EYE_GAZE_SEGMENTATION_PATH = lambda dataset_path, patient_id, dicom_id, segmentation : os.path.join(dataset_path, "patient_" + str(patient_id), "EyeGaze", "audio_segmentation_transcripts", dicom_id, segmentation + ".png" )

	# reflacx ellipse annotations
	REFLACX_ELLIPSE_PATH = lambda dataset_path, patient_id, reflacx_id: os.path.join(dataset_path, "patient_" + str(patient_id), "REFLACX", reflacx_id, "anomaly_location_ellipses.csv" )
	REFLACX_FIXATIONS_PATH = lambda dataset_path, patient_id, reflacx_id : os.path.join(dataset_path, "patient_" + str(patient_id), "REFLACX", reflacx_id, "fixations.csv" )
	REFLACX_RAW_PATH = lambda dataset_path, patient_id, reflacx_id : os.path.join(dataset_path, "patient_" + str(patient_id), "REFLACX", reflacx_id, "gaze.csv" )
	REFLACX_FIXATIONS_SOURCE_PATH = lambda reflacx_path, reflacx_id : os.path.join(reflacx_path, "main_data", reflacx_id, "fixations.csv" )
	REFLACX_GAZE_SOURCE_PATH = lambda reflacx_path, reflacx_id : os.path.join(reflacx_path, "gaze_data", reflacx_id, "gaze.csv" )
	REFLACX_METADATA = lambda dataset_path, patient_id : os.path.join(dataset_path, "patient_" + str(patient_id), "REFLACX", "metadata.csv" )

	# reflacx transcripts
	REFLACX_TRANSCRIPTS_PATH = lambda dataset_path, patient_id, reflacx_id : os.path.join(dataset_path, "patient_" + str(patient_id), "REFLACX", reflacx_id, "timestamps_transcription.csv" )

	# reflacx chest annotation
	REFLACX_CHEST_ANNOTATION_PATH = lambda dataset_path, patient_id, reflacx_id : os.path.join(dataset_path, "patient_" + str(patient_id), "REFLACX", reflacx_id, "chest_bounding_box.csv" )


	# main path where MIMIC-EYE's state will be saved
	CACHE_PATH = os.path.join(".", "cache", "mimic_eye_state.pkl")
	
	# main unit of MIMIC-EYE where the dataset will be stored in memory
	CACHE = {
						"REFLACX" : 0,							# counts how many patients are in REFLACX dataset
						"EYE_GAZE" : 0,							# counts how many patients are in EYE GAZE dataset
						"EYE_GAZE_PATIENTS" : [],		# lists the patient ids that are in EYE GAZE dataset
						"REFLACX_PATIENTS" : [],		# lists the patient ids that are in REFLACX dataset
						"OVERLAP" : [],							# lists the patient ids that overlap both datasets
						"PATIENTS" : {},						# dictionary containing all information about a single patient
						"DICOM_TO_XRAY" : {},				# dictionary mapping a DICOMID to an XRay object"
						"XRAY_TO_PATIENT" 	: {},		# dictionary mapping an XRayID to a PatientID
						"XRAY_TO_DIAGNOSIS" : {},		# dictionary mapping an XRayID to a Diagnosis (Eye Gaze only)
	}

	# for display purposes ----------------------------------------------
	FONT = { 'family': 'Ubuntu', 'size': 12}

	COLORS = { "butter": [ '#fce94f', '#edd400', '#c4a000'],
			"orange": [ '#fcaf3e', '#f57900', '#ce5c00'],
			"chocolate": [ '#e9b96e', '#c17d11', '#8f5902'],
			"chameleon": [ '#8ae234', '#73d216', '#4e9a06'],
			"skyblue": [ '#729fcf', '#3465a4', '#204a87'],
			"plum": [ '#ad7fa8', '#75507b', '#5c3566'],
			"scarletred":[ '#ef2929', '#cc0000', '#a40000'],
			"aluminium": [ '#eeeeec', '#d3d7cf', '#babdb6', '#888a85', '#555753', '#2e3436'],}

	COLOR_MAP = {
    "CARDIAC SILHOUETTE" 			: "#C0392B",
		"ENLARGED CARDIAC SILHOUETTE" : "#D98880",
    "LEFT CLAVICLE" 					: "#AF7AC5",
    "RIGHT CLAVICLE" 					: "#AF7AC5",
    "LEFT COSTOPHRENIC ANGLE" : "#2471A3",
    "RIGHT COSTOPHRENIC ANGLE": "#2471A3",
    "LEFT HILAR STRUCTURES" 	: "#76D7C4",
    "RIGHT HILAR STRUCTURES" 	: "#76D7C4",
    "LEFT LOWER LUNG ZONE" 		: "#F4D03F",
    "RIGHT LOWER LUNG ZONE" 	: "#F4D03F",
    "LEFT LUNG" 							: "#F4F6F7",
    "RIGHT LUNG" 							: "#F4F6F7",
    "LEFT MID LUNG ZONE" 			: "#F39C12",
    "RIGHT MID LUNG ZONE" 		: "#F39C12",
    "LEFT UPPER LUNG ZONE" 		: "#27AE60",
    "RIGHT UPPER LUNG ZONE" 	: "#27AE60",
    "TRACHEA" 								: "#F9E79F",
    "UPPER MEDIASTINUM" 			: "#AED6F1",
		"OTHER" 									: "#F4F6F7",
		"CONSOLIDATION"						: "#F7DC6F",
		"PNEUMOTHORAX"						: "#5DADE2",
}
