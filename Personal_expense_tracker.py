
import os

expenses = []
records = "expense.txt"


def save_expense():
    file = open(records, "w")

    for expense in expenses:
        file.write(expense["name"] + ",")
        file.write(str(expense["amount"]) + ",")
        file.write(expense["category"] + "\n")

    file.close()


def load_expenses():
    if os.path.exists(records):
        file = open(records, "r")

        for line in file:
            data = line.strip().split(",")

            expense = {
                "name": data[0],
                "amount": float(data[1]),
                "category": data[2]
            }

            expenses.append(expense)

        file.close()


def add_expenses():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expense()

    print("Expense added successfully")


def view_expenses():
    if not expenses:
        print("No expenses recorded")
        return

    for expense in expenses:
        print("\nExpense_name:", expense["name"])
        print("Expense_amount:", expense["amount"])
        print("Expense_category:", expense["category"])


def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total expense is:", total)


def expense_by_category():
    category = input("Enter expense category: ")
    total_category = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total_category += expense["amount"]

    print("Total category expense is:", total_category)


def highest_expense():
    if not expenses:
        print("No expenses recorded")
        return

    highest_expense = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest_expense["amount"]:
            highest_expense = expense

    print("Highest Expense:")
    print("Name:", highest_expense["name"])
    print("Amount:", highest_expense["amount"])
    print("Category:", highest_expense["category"])


# Load previously saved expenses
load_expenses()


while True:
    print("\n----MENU----")
    print("1. Add expense")
    print("2. View expense")
    print("3. Calculate total expense")
    print("4. Expense by category")
    print("5. Highest expense")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expenses()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        expense_by_category()
    elif choice == "5":
        highest_expense()
    elif choice == "6":
        print("Program terminated!! Thank you.")
        break
    else:
        print("Invalid choice")
