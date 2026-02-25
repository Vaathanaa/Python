import string
Password = input("Enter your password :")
Weak = 0
Moderate = 0
Uppercase = 0
SpecialCharector =0
if (len(Password) >= 8 ):
    Moderate = 1
else:
    Weak =1 
for char in Password:
    if char.isupper():
        Uppercase = 1
        break  
for char in Password:
    if char in string.punctuation:
        SpecialCharector = 1
        break
if SpecialCharector and Uppercase and Moderate :
    print("The password is Strong")
elif Moderate:
    print("The password is Moderate ")
elif Weak:
    print("The password is weak")
    
    
    
import string
def isValidPassword(password):
       hasUpper = any(char.isupper() for char in password)
       hasLower = any(char.islower() for char in password)
       hasSpecial = any(char in string.punctuation for char in password)
       text_len = len(password)
       if(text_len < 8):
              return "Weak"
       elif(hasUpper and hasLower and hasSpecial):
              return "Strong"
       else:
              return "Moderate"
       
       
password = input("Enter Your Password: ")
password_strength = isValidPassword(password)
print(f"Password Strength : {password_strength}")