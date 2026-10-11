print("Welcome to our restaurant. Here's the menu:")
print("Pizza: Rs40")
print("Pasta: Rs50")
print("Burger: Rs60")
print("Salad: Rs70")
print("Coffee: Rs80")

Food = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80
}

Total = 0

while True:
    order_food = input("Enter the item you want to order: ")

    if order_food not in Food:
        print("Item not available! Please order another item.")
        continue

    print(f"{order_food} has been added to your order.")
    Total += Food[order_food]

    more_order = input("Do you want to order anything else? (Yes/No): ")

    if more_order.lower() == "no":
        break

print(f"\nYour total bill is Rs.{Total}")