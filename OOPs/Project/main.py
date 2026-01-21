class chatbook:
    __user_id = 0   # encapsuted class variable

    def __init__(self):
        self.id = chatbook.__user_id    # setter = id
        chatbook.__user_id += 1
        self.__name = "Default User"     # private attribute aka encapsulated attribute
        self.username = ''
        self.email = ''
        self.password = ''
        self.login_status = False
        # self.menu()

    # getter and setter methhods for the private attribute __name and __user_id

    def get_id(self):
        return chatbook.__user_id

    def set_id(self, val):
        chatbook.__user_id = val
        return chatbook.__user_id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def menu(self):
        user_input = input(""""Welcome to Chatbook
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           -> """)
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.message_friend()
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
        print(
            f"Your username is {self.username}, password is {self.password} and mail is {self.email}")
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

    def write_post(self):
        if self.login_status == True:
            post = input("Write your post here: ")
            print("\n")
            print(f"Your post has been published successfully: {post}")
        else:
            print("\nYou are not signned in, please sign in first to write a post")
            print("\n")
            self.menu()

    def message_friend(self):
        if self.login_status == True:
            friend_name = input("Please enter your friend name here: ")
            msg = input("\nEnter your message here:")
            print(
                f"\nYour message has been succesfully sent to {friend_name} : {msg}")
            print("\n")
        else:
            print(
                "you are not siggned in or signned up yet. Please sign in or sign up first to send any message")
            print("\n")
            self.menu()


# creating an object instance of the class
obj = chatbook()
