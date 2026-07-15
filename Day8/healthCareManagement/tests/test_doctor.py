import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from data.datastore import datastore
from models.doctor import Doctor
from services.doctor_service import DoctorService


def setup_function():
    datastore["patients"].clear()
    datastore["doctors"].clear()
    datastore["appointments"].clear()


def test_add_and_get_doctor():
    service = DoctorService(datastore)
    doctor = Doctor(10, "Dr. Smith", 45, "Cardiology")

    service.add_doctor(doctor)

    assert service.get_doctor(10) == "ID: 10, Name: Dr. Smith, Age: 45, Specialty: Cardiology"


def test_update_and_delete_doctor():
    service = DoctorService(datastore)
    doctor = Doctor(11, "Dr. Jane", 38, "Neurology")
    service.add_doctor(doctor)

    service.update_doctor(11, "Pediatrics")
    assert datastore["doctors"][11].specialty == "Pediatrics"

    service.delete_doctor(11)
    assert service.get_doctor(11) is None
