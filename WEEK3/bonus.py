def secure_password(password):
    charecter_password = len(password)
    has_digit = False
    has_upper = False
    has_symbol = False
    strong_password = False
    for i in password:
        if i.isdigit():
            has_digit = True
        if i.isupper():
            has_upper = True
        if not i.isalpha() and not i.isdigit():
            has_symbol = True
    if charecter_password >= 8 and has_digit and has_upper and has_symbol:
        print("Registration successful with a strong password!")
        strong_password = True
    elif charecter_password >= 8 and has_digit and has_upper:
        print("Password must contain at least one special letter.")
    elif charecter_password >= 8 and has_digit:
        print("Password must contain at least one uppercase.")
    elif charecter_password >= 8 and has_upper:
        print("Password must contain at least one digit.")
    elif charecter_password >= 8:
        print("Password must atleast contain one uppercase and one digit.")
    elif charecter_password < 8:
        print("Password must atleast 8 letter.")
    return strong_password

def register(usernames):
    check_password = False
    username = input("Enter a username to register: ")
    for x in usernames:
        if username == x["Username"]:
            print("Username already exist.")
            check_password = True
    while check_password != True:
        password = input("Enter a password: ")
        check_password = secure_password(password)
        if check_password:
            new_account = {"Username": username, "Password": password}
            usernames.append(new_account)

def login(usernames):
    attempts = 3
    while attempts > 0:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for x in usernames:
            if username == x["Username"] and password == x["Password"]:
                print(f"Login successful! Welcome, {username}.")
                attempts = -1
        if attempts == -1:
            break
        attempts -= 1
        print(f"Invalid credentials. You have {attempts} attempts left.")
    if attempts == 0:
        print("Too many failed attempts. Access blocked.")

def forgot_password(usernames):
    username = input("Enter your username to retrieve your password: ")
    exist = True
    for x in usernames:
        if username == x["Username"]:
            print(f"Your password is: {x["Password"]}")
            exist = False
    if exist:
        print("Your username doesn't exist.")

def menu():
    print("1. Register")
    print("2. Login")
    print("3. Forgot Password")
    print("4. Exit")

usernames = [{"Username": "Window", "Password": "Hello, window11"}]
options = 0

while options != 4:
    menu()
    options = int(input("Choose an option(1-4): "))
    match options:
        case 1:
            register(usernames)
        case 2:
            login(usernames)
        case 3:
            forgot_password(usernames)