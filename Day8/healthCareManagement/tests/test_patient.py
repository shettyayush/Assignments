import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from data.datastore import datastore
from models.patient import Patient
from services.patient_service import PatientService


def setup_function():
    datastore["patients"].clear()
    datastore["doctors"].clear()
    datastore["appointments"].clear()


def test_add_and_get_patient():
    service = PatientService(datastore)
    patient = Patient(1, "Alice", 30, "Flu")

    service.add_patient(patient)

    assert service.get_patient(1) == "ID: 1, Name: Alice, Age: 30, Ailment: Flu"


def test_update_and_delete_patient():
    service = PatientService(datastore)
    patient = Patient(2, "Bob", 40, "Cold")
    service.add_patient(patient)

    service.update_patient(2, "Migraine")
    assert datastore["patients"][2].ailment == "Migraine"

    service.delete_patient(2)
    assert service.get_patient(2) is None
