from services.appointment_service import AppointmentService
from services.doctor_service import DoctorService
from services.patient_service import PatientService


class HealthcareSystem:
    def __init__(self, datastore):
        self.patient_service = PatientService(datastore)
        self.doctor_service = DoctorService(datastore)
        self.appointment_service = AppointmentService(datastore)