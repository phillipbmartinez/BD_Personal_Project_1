# 1. Greet user, ask for their user name, log in or create account. Keep logged in until they log out

#2 Ask what they would like to do: check accounts, deposit, transfer, get money, etc.

from prettytable import PrettyTable

def stay_logged_in(stay_logged_in):
    if stay_logged_in == "yes":
        return True
    elif stay_logged_in == "no":
        return False
    else:
        print("Invalid response.")
        return True

# def get_user_account_info(user_username, user_password):
#     if user_username != "create":
#         user_password = input("Please enter your password: ")
#         return user_username, user_password
#     elif user_username == "create":
#         user_username = input("What would you like your username to be? ").lower()
#         user_password = input("What would you like your password to be? ").lower()
#         return user_username, user_password
#     else:
#         print("Invalid response, exiting portal.")
#         return False

def user_login(user_username, user_password):
    bank_user_names = {"pmartinez": "test",
                       "rlira": "test",}
    if user_username not in bank_user_names:
        bank_user_names[user_username] = user_password
        print("New account created. You're now logged in.")
        print("***************************** \n")
        print(bank_user_names)
    elif (user_username in bank_user_names) and (user_password == bank_user_names.get(user_username)):
        print("You're now logged in.")
        print("***************************** \n")
    else:
        print("Username and/or password did not match, exiting portal.")



def main():
    balance = 0
    is_running = True

    print("Hello! Welcome to the Python Bank web portal!")
    user_username = input("If you have an account with us, please enter it now. If you don't have an account, please type 'Create': ").lower()
    if user_username != "create":
        user_password = input("Please enter your password: ")
    elif user_username == "create":
        user_username = input("What would you like your username to be? ").lower()
        user_password = input("What would you like your password to be? ").lower()
    else:
        print("Invalid response, exiting portal.")

    user_login(user_username, user_password)

    while is_running:
        table = PrettyTable()
        table.add_column("Action", ["View Balance", "Withdraw", "Deposit", "Transfer", "Log Out"])
        table.add_column("Code", ["1", "2", "3", "4", "5"])
        # table.add_row(["Action", "Code"])
        print(table)
        user_action = input("What would you like to do today? ").lower
        if user_action == 1:
            pass
        elif user_action == 2:
            pass
        elif user_action == 3:
            pass
        elif user_action == 4:
            pass
        elif user_action == 5:
            pass
        else:
            print("Invalid response.")



main()


