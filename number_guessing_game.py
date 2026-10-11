import random
a=random.randint(1,100)
while True:
    try:
        your_number=int(input("Guess a number:"))

        if(your_number>a):
            print("Guess Lower")
        elif(your_number<a):
            print("Guess Higher")
        else:
            print(f"Congratulations you guessed the correct number which was {a} ")
            break
    except ValueError:  
        print("Enter a valid number")
    