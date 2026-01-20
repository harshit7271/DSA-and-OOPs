class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.login_status = False
        self.menu()

    def menu(self):
        user_input = input(""""Welcome to Chatbook
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit""")
        if user_input == '1':
            pass
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            print("Thaanks for using ChatBook")


# creating an object instance of the class
app = chatbook()
