class chatbook:
    def __init__(self):
        self.username = ''
        self.email = ''
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
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            print("Thaanks for using ChatBook")

    def signup(self):
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.username = username
        self.email = email
        self.password = password
        print("Signup successfull")
        print("\n")
        print(f"Your username is {self.username} and email is {self.email}")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.email == '' and self.password == '':
            print("You are not signned up yet. Please signup first")
            print("\n")
            self.menu()
        else:
            uname = input("Enter your username: ")
            pwd = input("Enter your password: ")
            email = input("Enter your email: ")
            if uname == self.username and pwd == self.password and email == self.email:
                print("Signin successfull")
                self.login_status = True
            else:
                print("signin failed. Wrong credentials")
        print("\n")
        self.menu()


# creating an object instance of the class
app = chatbook()
