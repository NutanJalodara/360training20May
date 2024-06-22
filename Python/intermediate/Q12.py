def login_system():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    attempts = 0
    while attempts < 3:
        entered_password = input("Re-type your password: ")
        if entered_password == password:
            print("Login successful")
            return
        else:
            attempts += 1
            print(f"Incorrect password. You have {3 - attempts} attempt(s) left.")
    print("Too many failed attempts.")

login_system()
