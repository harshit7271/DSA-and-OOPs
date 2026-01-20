# Initiate class
class employee():
    # special method/magic method/dunder method - constructor
    def __init__(self):
        self.id = 102
        self.designation = "ML Engineer"
        self.salary = 75000


# create an object instance of the class
sam = employee()
print(sam.designation)
