from data.datastore import datastore
from models.doctor import Doctor
from models.patient import Patient
from services.healthcare_system import HealthcareSystem
from utils.logger import log_info


def main():
    system = HealthcareSystem(datastore)

    patient1 = Patient(1, "John Doe", 30, "Flu")
    patient2 = Patient(2, "Jane Smith", 25, "Cold")

    doctor1 = Doctor(101, "Dr. Smith", 45, "Cardiology")
    doctor2 = Doctor(102, "Dr. Patel", 38, "Neurology")

    system.patient_service.add_patient(patient1)
    system.patient_service.add_patient(patient2)
    system.doctor_service.add_doctor(doctor1)
    system.doctor_service.add_doctor(doctor2)

    appointment = system.appointment_service.book_appointment(1, 101, "2026-07-15", "10:00")

    log_info("Healthcare system initialized")
    log_info(f"Appointment booked: {appointment.display_info()}")

    print("Patient 1:", system.patient_service.get_patient(1))
    print("Patient 2:", system.patient_service.get_patient(2))
    print("Doctor 101:", system.doctor_service.get_doctor(101))
    print("Appointment:", system.appointment_service.get_appointment(appointment.id))


if __name__ == "__main__":
    main()