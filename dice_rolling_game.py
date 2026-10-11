import random

while True:
    choice=input("Roll the Dice(Y/N): ").lower()
    if(choice=="y"):
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"You have rolled{die1} and {die2}")

    elif(choice=="n"):
        print("Thanks for playing")
        break

    else:
        print("Invalid Choice!!")
    

