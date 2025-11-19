class chatbook:
    __user_id=1
    def __init__(self):
        self.id=chatbook.__user_id
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.__name = 'Default User'   # initialize private name
    @staticmethod
    def get_id():
        return chatbook.__user_id
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def menu(self):
        while True:
            user_input = input("""Welcome to Chatbox !! How would you like to proceed?
                1. Press 1 to signup
                2. Press 2 to signin
                3. Press 3 to write a post
                4. Press 4 to message a friend
                5. Press any other key to exit
            """)
            if user_input == "1":
                self.signup()
            elif user_input == "2":
                self.signin()
            elif user_input == "3":
                self.my_posts()
            elif user_input == "4":
                self.sendmsg()
            else:
                break

    def signup(self):
        email = input("Enter your email: ")
        pwd = input("Enter your password: ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!\n")

    def signin(self):
        if self.username == '' and self.password == '':
            print("No user found, please signup first")
        else:
            uname = input("Enter your email/username here -> ")
            pwd = input("Enter your password here -> ")
            if self.username == uname and self.password == pwd:
                print("You have signed in successfully !!")
                self.loggedin = True
            else:
                print("Please input correct credentials...")
        print("\n")

    def my_posts(self):
        if self.loggedin:
            txt = input("Enter your message here -> ")
            print(f"Following is your post -> {txt}")
        else:
            print("You need to signin first to post something...")
        print("\n")

    def sendmsg(self):
        if self.loggedin:
            friend = input("Enter your friend's name here -> ")
            msg = input("Enter your message here -> ")
            print(f"Your message '{msg}' has been sent to {friend} successfully !!")
        else:
            print("You need to signin first to send a message...")
        print("\n")

obj = chatbook()
#obj.menu()
