from main import chatbook

user1 = chatbook()

print(user1.get_name())  # fetching the private attribute using getter method
# modifiying the private attribute using the setter method
user1.set_name("Garima")
print(user1.get_name())
print(user1.id)


user2 = chatbook()
user2.get_name()
user2.set_name("Harshit")
print(user2.get_name())
print(f"{user2.id}")
