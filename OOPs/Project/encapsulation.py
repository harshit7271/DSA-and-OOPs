from main import chatbook
"""
user1 = chatbook()
""""print(user1.__name)""""    # this will raise an AttributeError because __name is private (encapsulated)

# accessing the private attribute using name mangling
print(user1._chatbook__name)
print(user1.id)

user2 = chatbook()
print(user2.id)
"""

# ------------encapsulation using getter and setter methods----------------
user1 = chatbook()
print(user1.id)

chatbook.set_id(15)
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)
