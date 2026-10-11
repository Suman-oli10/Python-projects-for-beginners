import random
choices=("r","p","s")
emoji={"r":"👊","p":"📃","s":"✂️"}

while True:
    gamer_input=input("Rock, Paper, Scissors? (r/p/s): ").lower()
    if(gamer_input not in choices):
        print("Invalid Input")
        continue
    
    computer=random.choice(choices)
    
    if(computer==gamer_input):
        print(f"You chooses {emoji[gamer_input]} and computer chooses {emoji[computer]}, So its a tie!!")
    elif(
        (computer=="r" and gamer_input=="s")or
        (computer=="p" and gamer_input=="r")or
        (computer=="s" and gamer_input=="p")
        ):
        print(f"You chooses {emoji[gamer_input]} and computer chooses {emoji[computer]}, So computer win!!")
    else:
        print(f"You chooses {emoji[gamer_input]} and computer chooses {emoji[computer]}, So You win!!")

    continue_game=input("Would you like to continue(Y/N): ").lower()
    if(continue_game=="n"):
        print("Thanks for playing!!")
        break

