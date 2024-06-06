def get_user_account():
    print("Welcome!")
    user_username = input("Please enter your username: ").lower()
    user_password = input("Please enter your password: ")
    print("\n")

    user_login(user_username, user_password)

def user_login(user_username, user_password):
    bank_user_names = {"pmartinez": {"first name": "Phillip",
                "last name": "Martinez",
                "city": "San Antonio",
                "state": "Texas",
                "zip": 78148,
                "street": "236 Gamblewood",
                "password": "test",
                "username": "pmartinez"}}
    if user_username not in bank_user_names:
        print("No account found. Exiting application.")
        print("***************************** \n")
    elif (user_username in bank_user_names) and (user_password == bank_user_names[user_username]["password"]):
        print("You're now logged in.")
        print("***************************** \n")
    else:
        print("Username and/or password were not found or did not match. Exiting application.")

    for user in bank_user_names:
        print(f"Your username is: {bank_user_names[user]['username']}")
        print(f"Your password is: {bank_user_names[user]['password']}")
    
def main():
    get_user_account()

main()
    

