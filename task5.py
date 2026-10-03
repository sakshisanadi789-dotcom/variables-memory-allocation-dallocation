def is_valid_user(user, password):
    return user == "admin" and password == "python123"


user = input("Enter username: ")
password = input("Enter password: ")

if is_valid_user(user, password):
    print("Valid user")
else:
    print("Invalid user")
