
import random
import time

sentences = [
    "I wake up early in the morning.",
    "The sun rises in the east.",
    "She goes to school every day.",
    "My father works in an office.",
    "We should always speak the truth.",
    "Reading books improves our knowledge.",
    "The children are playing in the garden.",
    "I enjoy learning new things.",
    "Nepal is a beautiful country.",
    "Hard work is the key to success."
]


def test():
    typing_sentence = random.choice(sentences)

    print("\nType the following sentence:")
    print(typing_sentence)

    input("\nPress ENTER when you are ready...")

    starting_time = time.time()

    user_text = input("\nType here: ")

    end_time = time.time()

    elapsed_time = end_time - starting_time

    # Calculate typing speed
    total_words = len(user_text.split())
    elapsed_minutes = elapsed_time / 60

    if elapsed_minutes > 0:
        wpm = total_words / elapsed_minutes
    else:
        wpm = 0

    # Calculate typing accuracy
    correct_characters = 0
    total_characters = len(typing_sentence)

    for index in range(total_characters):
        if index < len(user_text):
            if typing_sentence[index] == user_text[index]:
                correct_characters += 1

    accuracy = (correct_characters / total_characters) * 100

    # Display results
    print("\n===== TEST RESULTS =====")
    print(f"Time Taken: {elapsed_time:.2f} seconds")
    print(f"Typing Speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

    if accuracy >= 95:
        print("Excellent typing accuracy!")
    elif accuracy >= 80:
        print("Good job! Keep practicing!")
    else:
        print("Keep practicing to improve your accuracy!")


while True:
    print("\n===== TYPING SPEED TEST =====")
    print("1. Start Test")
    print("2. Exit")

    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        test()

    elif user_choice == "2":
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice. Please try again.")
