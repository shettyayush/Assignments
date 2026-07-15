import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from data.datastore import datastore
from models.appointment import Appointment
from models.doctor import Doctor
from models.patient import Patient
from services.appointment_service import AppointmentService
from services.doctor_service import DoctorService
from services.patient_service import PatientService


def setup_function():
    datastore["patients"].clear()
    datastore["doctors"].clear()
    datastore["appointments"].clear()


def test_book_and_update_appointment():
    patient_service = PatientService(datastore)
    doctor_service = DoctorService(datastore)
    appointment_service = AppointmentService(datastore)

    patient_service.add_patient(Patient(1, "Alice", 30, "Flu"))
    doctor_service.add_doctor(Doctor(10, "Dr. Smith", 45, "Cardiology"))

    appointment = appointment_service.book_appointment(1, 10, "2026-07-15", "10:00")

    assert appointment.patient_id == 1
    assert appointment.doctor_id == 10
    assert appointment.status == "Scheduled"

    appointment_service.update_appointment_status(appointment.id, "Completed")
    updated = appointment_service.get_appointment(appointment.id)

    assert updated is not None
    assert updated["status"] == "Completed"
