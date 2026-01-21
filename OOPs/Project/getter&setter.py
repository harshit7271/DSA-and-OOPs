from main import chatbook

user1 = chatbook()

print(user1.get_name())  # fetching the private attribute using getter method

# modifiying the private attribute using the setter method
user1.set_name("Garima")

print(user1.get_name())
