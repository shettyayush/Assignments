from models.person import Person


class Patient(Person):
    def __init__(self, id, name, age, ailment):
        super().__init__(id, name, age)
        self.ailment = ailment

    def get_details(self):
        details = super().get_details()
        details.update({"ailment": self.ailment})
        return details

    def display_info(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Ailment: {self.ailment}"