# Add a method to the car class that displays the full name of the car (brand and model)-

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_details(self):
        return f"{self.brand}, {self.model}"


my_car = Car("Toyota", "Corolla")
# we will use paranthesis () to call method full_details
print(my_car.full_details())


# ----------------- Note : Advantages of OOPs-------------------
# Code resuability
# You craete your own data types
# Debugging is easier
# easy to colab
# self is nothing but the current object of the class that we will be replacing while creating the object instance of the class.
# It helps to access the attributes and methods of the class in python.
