questions=["1. Which planet is known as the Red Planet?",
           "2. Who developed the Python programming language?",
           "3. What is the largest ocean in the world?",
           "4. Which data structure stores data in key-value pairs in Python?",
           "5. What is the capital city of Australia?"]

Answers=["Mars","Guido Van Rossum","Pacific","Dictionary","Canberra"]

def clear_history():
    with open("results.txt","w") as file:
        print("History cleared\n")
        

while True: 
    score=0
    print("Welcome to Quiz game")
    name=input("Enter your name: ")
    for question in questions:
        print(question)
        user_choice=input("Enter the answer: ").lower()
        if user_choice==Answers[questions.index(question)].lower():
            print("Correct Answer!!\n")
            score+=1
        else:
            print("Wrong Answer!")
            print(f"The correct answer is {Answers[questions.index(question)].lower()}\n")

    print("Final Score is: ",score)
    percentage=(score/5)*100
    print("Percentage is: ",percentage)
    file=open("results.txt","a")
    file.write(f"Records of {name}:" + "\n")
    file.write(f"score is {score}" + "\n")
    file.write(f"percentage is {percentage}" + "\n\n")
    file.close()
    print("Result saved successfully\n")
    history=input("Do you want to clear history? (Y/N): ").lower()
    if history=="y":
        clear_history()
        
    choice=input("Do you want to play again? (Y/N): ").lower()
    if choice=="y":
        continue
    else:
        print("Thanks for playing!")
        break





