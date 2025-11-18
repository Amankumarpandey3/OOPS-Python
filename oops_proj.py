class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    

    def menu(self):
        user_input = input("""Welcome to Chatbox !! How would you like to proced?
                           1. Press 1 to signup
                           2. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()   

    def signup(self):
        email = input("Enter your email: ")
        pwd = input("Enter your password: ")
        self.username = email
        self.password = pwd
        print("your have signup successfully !!")
        print("\n")
        self.menu()
    def signin(self):
        if self.username=='' and self.password=='':
            print("No user found, please signup first")
        else:
            uname = input("enter your email/username here-> ")
            pwd = input("Enter your password here -> ")
            if self.username==uname and self.password==pwd:
                print("you have signed in successfully !!")
                self.loggedin =True
            else:
                print("Please input correct credentials...")

        print("\n")
        self.menu()

obj = chatbook()