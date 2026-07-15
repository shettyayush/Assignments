from models.appointment import Appointment


class AppointmentService:
    def __init__(self, datastore):
        self.datastore = datastore

    def book_appointment(self, patient_id, doctor_id, date, time):
        appointment_id = len(self.datastore["appointments"]) + 1
        appointment = Appointment(appointment_id, patient_id, doctor_id, date, time)
        self.datastore["appointments"][appointment_id] = appointment
        return appointment

    def get_appointment(self, appointment_id):
        appointment = self.datastore["appointments"].get(appointment_id)
        if appointment:
            return appointment.get_details()
        return None

    def update_appointment_status(self, appointment_id, status):
        if appointment_id in self.datastore["appointments"]:
            self.datastore["appointments"][appointment_id].status = status

    def delete_appointment(self, appointment_id):
        if appointment_id in self.datastore["appointments"]:
            del self.datastore["appointments"][appointment_id]