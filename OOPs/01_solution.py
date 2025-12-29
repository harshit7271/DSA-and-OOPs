# Creating a Car class with brand and model attributes and then create an instance of this class.

class Car:
    def __init__(self, brand, model):    # Constructor to initialize brand and model, self refers to the instance which create a link between attributes and parameters
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand)     

my_new_car = Car("Mahindra", "Scorpio N")
print(my_new_car.model)