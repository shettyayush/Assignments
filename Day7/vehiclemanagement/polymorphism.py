class Overlodingdemo:
    def show_details(self, *args):
        if len(args) == 1:
            print(f"Car Brand: {args[0]}")
        elif len(args) == 2:
            print(f"Car Brand: {args[0]}, Car Model: {args[1]}")
        elif len(args) == 3:
            print(f"Car Brand: {args[0]}, Car Model: {args[1]}, Car Year: {args[2]}")
        else:
            print("Invalid number of arguments. Please provide 1 to 3 arguments.")


def Overloadingdemo():
    demo = Overlodingdemo()
    demo.show_details("Toyota")
    demo.show_details("Tata", "Curvve")
    demo.show_details("BMW", "X5", 2022)
    demo.show_details("Honda", "Civic", 2021, "Extra Argument")  # Invalid case

Overloadingdemo()