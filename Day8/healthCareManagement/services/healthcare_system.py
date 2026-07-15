from services.patient_service import PatientService

class HealthcareSystem:
    def __init__(self, datastore):
        self.patient_service = PatientService(datastore)