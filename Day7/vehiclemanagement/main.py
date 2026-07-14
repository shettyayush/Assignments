from car import Car
from ev import EV
from polymorphism import Overloadingdemo
from report_export import export_vehicle_data
from exception import VehicleError
def main():
    try:
        car1 = Car("Toyota", "Vellfire", 2025)
        car2 = Car("Tata", "Curvve", 2026)
        car3 = Car("BMW", "X5", 2022, "Bob Johnson")
        car4 = EV("Tesla", "Model S", 2023, 100)

        car1.set_owner("Ankush")
        # car2.set_owner("Rohit")
        # car1.set_owner("Jon")
        car4.set_owner("Elon Musk")
        # car4.set_battery_capacity(-34)

        cars = [car1, car2, car3, car4]

        print("\n ---Overloading Demo ---")
        Overloadingdemo()

        print("\n ---Export Report ---")
        result = export_vehicle_data("vehicles.csv", cars)
        print(result)

        for car in cars:
            car.start_engine()
            car.show_info()
            print(f"Owner: {car.get_owner()}")
            if isinstance(car, EV):
                print(f"Battery Capacity: {car.battery_capacity} kWh")
            car.stop_engine()
            print()
    except VehicleError as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    main()


    