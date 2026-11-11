
students = []

def add_student():
    name = input("Enter student name: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("Student already exists")
            return

    marks = []

    for i in range(3):
        mark = int(input(f"Enter marks for subject {i + 1}: "))

        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100")
            return

        marks.append(mark)

    students.append({"name": name, "marks": marks})
    print("Student added successfully")


def display_students():
    if not students:
        print("No students found")
    else:
        for student in students:
            print("\nStudent name:", student["name"])
            print("Marks:", student["marks"])


def calculate_grade(student):
    total_marks = sum(student["marks"])
    average = total_marks / len(student["marks"])

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    return average, grade


def show_grade():
    name = input("Enter student name: ")

    for student in students:
        if student["name"].lower() == name.lower():
            average, grade = calculate_grade(student)

            print("Student name:", student["name"])
            print("Average marks:", average)
            print("Grade:", grade)
            return

    print("Student not found")


def search_student():
    name = input("Enter student name: ")

    for student in students:
        if student["name"].lower() == name.lower():
            average, grade = calculate_grade(student)

            print("Student name:", student["name"])
            print("Marks:", student["marks"])
            print("Average:", average)
            print("Grade:", grade)
            return

    print("Student not found")


def display_top_student():
    if not students:
        print("No students available")
    else:
        top_student = students[0]
        highest_average = calculate_grade(top_student)[0]

        for student in students:
            average, grade = calculate_grade(student)

            if average > highest_average:
                highest_average = average
                top_student = student

        average, grade = calculate_grade(top_student)

        print("Top student:", top_student["name"])
        print("Average marks:", average)
        print("Grade:", grade)


while True:
    print("\n===== STUDENT GRADE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Calculate Student Grade")
    print("4. Search Student")
    print("5. Display Top Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        show_grade()

    elif choice == "4":
        search_student()

    elif choice == "5":
        display_top_student()

    elif choice == "6":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
