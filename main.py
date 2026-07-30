import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except:
                return []
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    students = load_students()

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)

    print("\nStudent Added Successfully!\n")


def view_students():
    students = load_students()

    if not students:
        print("\nNo Students Found!\n")
        return

    print("\nStudent Records")
    print("-" * 40)

    for student in students:
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
        print("-" * 40)


def search_student():
    students = load_students()

    student_id = input("Enter Student ID to Search: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found")
            print(student)
            return

    print("\nStudent Not Found!\n")


def delete_student():
    students = load_students()

    student_id = input("Enter Student ID to Delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("\nStudent Deleted Successfully!\n")
            return

    print("\nStudent Not Found!\n")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
