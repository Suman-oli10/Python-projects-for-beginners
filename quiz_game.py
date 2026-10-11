
questions = [
    {
        "question": "1. Which language is used for AI?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. SQL"],
        "answer": "B"
    },
    {
        "question": "2. What is the brain of a computer?",
        "options": ["A. CPU", "B. Mouse", "C. Keyboard", "D. Monitor"],
        "answer": "A"
    },
    {
        "question": "3. Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. List"],
        "answer": "C"
    },
    {
        "question": "4. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. <!-- -->", "D. **"],
        "answer": "B"
    },
    {
        "question": "5. Which function displays output in Python?",
        "options": ["A. input()", "B. print()", "C. output()", "D. show()"],
        "answer": "B"
    }
]

score = 0

print("==============================")
print("       PYTHON QUIZ GAME")
print("==============================")
print("Choose the correct option: A, B, C, or D.\n")

for question in questions:
    print(question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Your answer: ").strip().upper()

    if answer == question["answer"]:
        print("Correct answer!\n")
        score += 1
    elif answer in ["A", "B", "C", "D"]:
        print("Wrong answer!\n")
    else:
        print("Invalid option. No point awarded.\n")

print("==============================")
print("         QUIZ RESULT")
print("==============================")
print("Your score:", score, "/", len(questions))
print("Percentage:", round(score / len(questions) * 100, 2), "%")

if score == len(questions):
    print("Excellent! Perfect score!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing!")

print("Thank you for playing!")
