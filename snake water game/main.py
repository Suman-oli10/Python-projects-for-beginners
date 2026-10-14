'''
1 = water
-1 = snake
0 = gun
'''

import random
computer=random.choice([0, 1, -1])
youstr=input("Enter your choice: ")
youdict={"s": -1, "w": 1, "g": 0}
reversedict={-1: "snake", 1: "water", 0: "gun"}

you=youdict[youstr]

print(f"You choose {reversedict[you]}\ncomputer choose {reversedict[computer]}")

if you==computer:
    print("It's a tie")

    if((you==1 and computer==-1) or (you==-1 and computer==0) or (you==0 and computer==1)):
        print("You loose!")
    elif(you==0 and computer==-1) or (you==-1 and computer==1) or (you==1 and computer==0):
        print("You win!")
    else:
        print("Something went wrong. Try again!")


