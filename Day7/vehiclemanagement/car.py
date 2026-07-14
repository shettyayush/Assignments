from exception import OwnerAlreadyExistsError
class Car:
    def __init__(self, brand, model, year, owner=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.__owner = owner #Private attribute to store the owner of the car
    def start_engine(self):
        print(f"The engine of the {self.brand} {self.model} is starting........")
    
    def show_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def stop_engine(self):
        print(f"The engine of the {self.brand} {self.model} is stopping.........")
    
    def set_owner(self, owner):
        if not self.__owner:
            self.__owner = owner
        else:
            raise OwnerAlreadyExistsError(self.__owner)
    
    def get_owner(self):
        return self.__owner
