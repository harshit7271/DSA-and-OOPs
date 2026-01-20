# Initiate class
class employee:
    # special method/magic method/dunder method - constructor (constructor get called automatically as we assign value to the object)
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 102
        self.designation = "ML Engineer"
        self.salary = 75000
        print("Attributes has been initiated successfully")

    def travel(self, destination):
        print("This travel function was called manually")
        print(f"The employee is traveling to {destination}")


# create an object instance of the class
sam = employee()
# printing the attribute
print(sam.designation)

# calling the method
sam.travel("New Delhi")
