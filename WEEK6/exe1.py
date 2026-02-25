class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_username(self): #display username
        print(f"Username: {self.username}")

    def verify_password(self):
        password = input("Password: ") #input password
        if self.__password == password: #this line to check the input password 
            print("Password Verified: True")
        else:
            print("Password Verified: False")

U = User("CADT", "Cyber@123")
U.get_username()
U.verify_password()