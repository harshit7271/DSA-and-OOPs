# Initiate class
class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        self.id = 102
        self.designation = "ML Engineer"
        self.salary = 75000

    def travel(self, destination):
        print(f"The employee is traveling to {destination}")


# create an object instance of the class
sam = employee()
# printing the attribute
print(sam.designation)

# calling the method
sam.travel("New Delhi")
