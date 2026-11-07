balance = 10000
pin = "2005"
attempt = 0
statement = "transaction.txt"

print("Welcome to ATM simulator")


def transaction(message):
    with open(statement, "a") as file:
        file.write(message + "\n")


while attempt < 3:
    password = input("Enter pin number: ")

    if pin == password:
        print("PIN verified successfully")

        while True:
            print("===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("Current Balance:", balance)

            elif choice == "2":
                deposit_amount = float(input("Enter deposit amount: "))

                if deposit_amount > 0:
                    balance += deposit_amount
                    print("Money deposited successfully")
                    print("Updated Balance:", balance)

                    transaction(f"Deposited: Rs. {deposit_amount}")

                else:
                    print("Invalid deposit amount")

            elif choice == "3":
                withdraw_amount = float(input("Enter withdrawal amount: "))

                if withdraw_amount <= 0:
                    print("Invalid withdrawal amount")

                elif withdraw_amount > balance:
                    print("Insufficient Balance")

                else:
                    balance -= withdraw_amount
                    print("Money withdrawn successfully")
                    print("Updated Balance:", balance)

                    transaction(f"Withdrawn: Rs. {withdraw_amount}")

            elif choice == "4":
                confirmation = input("Enter current PIN: ")

                if confirmation == pin:
                    new_pin = input("Enter new PIN: ")
                    pin = new_pin
                    print("PIN successfully changed")

                else:
                    print("Incorrect current PIN")

            elif choice == "5":
                print("Thank you for using ATM")
                break

            else:
                print("Invalid choice")

        break

    else:
        attempt += 1
        print("Wrong password, Try Again!")

if attempt == 3:
    print("Maximum attempts reached")
    print("ATM access denied")