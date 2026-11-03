import os
students=[]
records="student_records.csv"

def save_students():
    file = open(records, "w")

    for student in students:
        file.write(student["student_id"] + ",")
        file.write(student["name"] + ",")
        file.write(student["age"] + ",")
        file.write(student["marks"] + "\n")

    file.close()

def load_students():
    if os.path.exists(records):
        file = open(records, "r")

        for line in file:
            data = line.strip().split(",")

            student = {
                "student_id": data[0],
                "name": data[1],
                "age": data[2],
                "marks": data[3]
            }

            students.append(student)

        file.close()

def add_student():
    student_id=input("Stduent ID: ")
    for student in students:
        if student["student_id"]==student_id:
            print("Student already exists")
            return
    student_name=input("Student Name: ")
    student_age=input("Studetn Age: ")
    student_mark=input("Student Mark: ")

    student = {
        "student_id": student_id,
        "name": student_name,
        "age": student_age,
        "marks": student_mark
    }

    students.append(student)
    save_students()

    print("student added successfully")

def view_students():
    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\nStudent ID:", student["student_id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])


def search_student():
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["student_id"] == student_id:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["student_id"] == student_id:

            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Marks")

            choice = input("Enter your choice: ")

            if choice == "1":
                student["name"] = input("Enter new name: ")

            elif choice == "2":
                student["age"] = input("Enter new age: ")

            elif choice == "3":
                student["marks"] = input("Enter new marks: ")

            else:
                print("Invalid choice.")
                return

            save_students()
            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["student_id"] == student_id:

            students.remove(student)
            save_students()

            print("Student deleted successfully!")
            return

    print("Student not found.")


def calculate_average():
    if not students:
        print("No student records found.")
        return

    total_marks = 0

    for student in students:
        total_marks += float(student["marks"])

    average = total_marks / len(students)

    print("Average Marks:", round(average, 2))


load_students()



def main():
    while True:
        print("Welcome to the student Record Management System")
        print("1. Add Student\n2. View All sudent\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Calculate Average Marks\n7. Exit")
        user_choice=int(input("Enter your choice: "))
        if user_choice==1:
            add_student()
        elif user_choice==2:
            view_students()
        elif user_choice==3:
            search_student()
        elif user_choice==4:
            update_student()
        elif user_choice==5:
            delete_student()
        elif user_choice==6:
            calculate_average()
        elif user_choice == 7:
            print("Program terminated")
            break
        else:
            print("Invalid choice")

main()
        
    


