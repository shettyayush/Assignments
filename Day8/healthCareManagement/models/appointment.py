class Appointment:
    def __init__(self, id, patient_id, doctor_id, date, time, status="Scheduled"):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.status = status

    def get_details(self):
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "date": self.date,
            "time": self.time,
            "status": self.status,
        }

    def display_info(self):
        return (
            f"ID: {self.id}, Patient ID: {self.patient_id}, Doctor ID: {self.doctor_id}, "
            f"Date: {self.date}, Time: {self.time}, Status: {self.status}"
        )