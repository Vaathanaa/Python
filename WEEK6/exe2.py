class UserProfile:
    def __init__(self, username, phone_number):
        self.username = username
        self.__phone_number = phone_number
        
    def get_phone_number(self):
        return "XXXX-XXXX-" + self.__phone_number[-4:]# hide First 8 digit
    
    def display_public_info(self): #to display username and phonenumber
        print(f"Username : {self.username}")
        print(f"Phone number: {self.get_phone_number()}")
        
    def update_phone_number(self):
        inputphonenumber = input("Verify your old phonenumber: ") 
        if self.__phone_number == inputphonenumber: #verify phone number
            newphonenumber = input("Enter the new phone number: ")
            self.__phone_number = newphonenumber
            print("Contact Info Updated Successfull")
        else:
            print("Contact Info doesn't match")
            
U=UserProfile("CADT","1234-4214-4546")
U.display_public_info()
U.update_phone_number()
U.display_public_info()