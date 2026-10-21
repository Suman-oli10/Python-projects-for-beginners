import random

subject = ["KP Oli", "Sher Bahadur Deuba", "Ram Chandra Paudel",
           "Pradeep Gyawali", "Narayan Khadka",
           "Bimalendra Nath Sharma", "Gagan Thapa",
           "Ram Kumar Rai", "Shankar Pokharel", "Bishnu Prasad Paudel"]

Actions = ["dances with a goat", "sings to a potato",
           "jumps over a buffalo", "runs after a chicken",
           "swims in a bucket", "paints a flying momo",
           "writes love letters to a cow",
           "reads the newspaper upside down",
           "cooks noodles for aliens",
           "drives a toy car to the moon"]

places = ["on the roof of Singha Durbar",
          "inside a giant momo",
          "on Mount Everest wearing slippers",
          "in a buffalo's wedding ceremony",
          "at a secret meeting of monkeys",
          "in the middle of a potato farm",
          "inside a flying school bus",
          "at a UFO parking lot",
          "in a swimming pool full of tea",
          "on the moon with a pressure cooker"]

while True:
    print("\n Breaking News!")

    person = random.choice(subject)
    action = random.choice(Actions)
    place = random.choice(places)

    print(f"Breaking News: {person} {action} {place}!")

    user_input = input("Do you want another hot news? (Y/N): ")

    if user_input.upper() == "Y":
        continue
    else:
        break

print("Thanks for watching Nepali Funny News!")


