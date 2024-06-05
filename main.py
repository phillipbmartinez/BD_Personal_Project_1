# 1. Greet user, ask for their user name, log in or create account. Keep logged in until they log out

#2 Ask what they would like to do: check accounts, deposit, transfer, get money, etc.

from prettytable import PrettyTable

def get_user_account():
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

def user_login(user_username, user_password):
    bank_user_names = {"pm": "test",
                       "rlira": "test",
                       "pmartinez": "test"}
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

def view_balance(balance):
    print(f"Your balance is: ${balance:.2f} \n")

def withdraw(balance):
    amount = float(input("How much money would you like to withdraw? "))

    if amount < 0:
        print("Invalid response.")
        return 0
    elif amount > balance:
        print("Insufficient funds.")
        return 0
    else:
        balance -= amount
        print(f"Your balance is now: ${balance:.2f}\n")
        return amount

def deposit(balance):
    amount = float(input("How much money would you like to deposit? "))

    if amount < 0:
        print("Invalid response.")
        return 0
    else:
        balance += amount
        print(f"Your balance is now: ${balance:.2f}\n")
        return amount

def transfer(balance):
    amount = float(input("How much money would you like to transfer? "))
    account_number = input("What is the account number that you would like to transfer to? ")

    if amount < 0:
        print("Invalid response.")
        return 0
    else:
        balance -= amount
        print(f"Your balance is now: ${balance:.2f}\n")
        return amount

def print_menu():
        table = PrettyTable()
        table.add_column("Action", ["View Balance", "Withdraw", "Deposit", "Transfer", "Log Out"])
        table.add_column("Code", ["1", "2", "3", "4", "5"])
        print(table)

def main():
    balance = 0
    is_running = True

    get_user_account()

    while is_running:
        print_menu()

        user_action = input("What would you like to do today? ")
        if user_action == "1":
            view_balance(balance)
        elif user_action == "2":
            balance -= withdraw(balance)
        elif user_action == "3":
            balance += deposit(balance)
        elif user_action == "4":
            balance -= transfer(balance)
        elif user_action == "5":
            is_running = False
        else:
            print("Invalid response. Please try again.")
    print("Thank you, have a nice day.")


if __name__ == '__main__':
    main()


