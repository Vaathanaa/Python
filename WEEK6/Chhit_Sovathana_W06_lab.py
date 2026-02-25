#Exercise 1
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

#Exercise 2
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
#Exercise 3
class Malware:
    def describe(self):
        return "This is a malware."
class ransomware(Malware):# ransomware inherit from malware
    def encrypt_files(self):
        return "File are being encrypted."

m = Malware()
r = ransomware()
print(f"Malware Description: {m.describe()}")
print(f"Ransomware Description: {r.describe()}")
print(f"Ransomware Action: {r.encrypt_files()}")

#Exercise 4
class Malware:
    def describe(self):
        return "This is a malware."
class ransomware(Malware): #ransomware inherit from Malware
    def encrypt_files(self):
        return "File are being encrypted."
class virus(Malware):#virus inherit from Malware
    def replicate(self):
        return "Virus is replicating."
class trojan(Malware):#trojan inherit from Malware
    def hide_in_file(self):
        return "Hiding in files."
class keyLogger(trojan): #keylogger inherit from trojan
    def describe(self):
        return "This a keylogger. Capturing keystrokes."
    
m = Malware()
r = ransomware()
v = virus()
t = trojan()
k = keyLogger()

print(f"Virus Description: {v.describe()}")
print(f"Virus Action: {v.replicate()}")
print(f"Trojan Description: {t.describe()}")
print(f"Trojan Action: {t.hide_in_file()}")
print(f"Keylogger Description: {k.describe()}")
print(f"keylogger Action: {k.hide_in_file()}")

#Exercise 5
class Logger:
    def log(self):
        return "Error"

class Log(Logger):
    def log(self):
        return "Log: System started."
    
class ErrorCode(Logger):
    def log(self):
        return "Error Code: 404, Details: {'url': '/not-found'}."

class Message(Logger):
    def log(self):
        return "Unknown log format."
# Polymorphism function 
def loggin(logger):
    print(logger.log())

L = Log()
E = ErrorCode()
M = Message()

#  Use Polymorphism
loggin(L)
loggin(E)
loggin(M)

#Exercise 6

class FirewallRule:
    def apply_rule(self):
        return "Applying generic rule."

class IPBlockRule(FirewallRule):
    def apply_rule(self):
        return "Block IP Address."

class PortBlockRule(FirewallRule):
    def apply_rule(self):
        return "Block port number."

#Polymorphism function
def firewall_action(rule):
    print(f"Firewall Action: {rule.apply_rule()}")
    
f = FirewallRule()
i = IPBlockRule()
p = PortBlockRule()
#polymorphism use
firewall_action(f)
firewall_action(i)
firewall_action(p)