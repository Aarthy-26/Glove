patient_records = {}

def store_patient_data(patient_id, data):
    """Stores patient data."""
    patient_records[patient_id] = data

def get_patient_data(patient_id):
    """Retrieves stored patient data."""
    return patient_records.get(patient_id, "No data found")


