class Student:
    def __init__(self , roll , name , marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def to_string(self):
        return f"{self.roll} , {self.name} , {self.marks}\n"
    
def add_student():
    roll = input("Enter Roll Number : ")
    name = input("Enter Name : ")
    marks = input("Enter Marks : ")

    if not marks.isdigit():
        print("Marks must be a number")
        return


    student = Student(roll , name , marks)

    with open("students.txt","a") as file:
        file.write(student.to_string())

    print("Student added succesfully!")

def view_students():
    try:
        with open("students.txt","r") as file:
            students = file.readlines()

        if not students:
            print("No student record found.")
            return
        
        print("\nRoll\tName\tMarks")
        print("-"*25)

        for student in students:
            roll , name,marks = student.strip().split(",")
            print(f"{roll}\t{name}\t{marks}")

    except FileNotFoundError:
        print("No data file found")

def search_student():
    roll_to_search = input("Enter roll number to search: ").strip()
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                roll, name, marks = [x.strip() for x in line.split(",")]

                if roll == roll_to_search:
                    print("\nStudent Found:")
                    print(f"Roll: {roll}")
                    print(f"Name: {name}")
                    print(f"Marks: {marks}")
                    found = True
                    break

        if not found:
            print("❌ Student not found.")

    except FileNotFoundError:
        print("No data file found.")

def update_student():
    roll_to_update = input("Enter roll number to update: ").strip()
    updated = False
    students = []

    try:
        with open("students.txt", "r") as file:
            for line in file:
                roll, name, marks = [x.strip() for x in line.split(",")]

                if roll == roll_to_update:
                    print("Enter new details:")
                    name = input("New Name: ")
                    marks = input("New Marks: ")
                    students.append(f"{roll},{name},{marks}\n")
                    updated = True
                else:
                    students.append(f"{roll},{name},{marks}\n")

        with open("students.txt", "w") as file:
            file.writelines(students)

        if updated:
            print("✅ Student updated successfully!")
        else:
            print("❌ Student not found.")

    except FileNotFoundError:
        print("No data file found.")


def delete_student():
    roll_to_delete = input("Enter roll number to delete: ").strip()
    deleted = False
    students = []

    try:
        with open("students.txt", "r") as file:
            for line in file:
                roll, name, marks = [x.strip() for x in line.split(",")]

                if roll == roll_to_delete:
                    deleted = True
                    continue  # skip this record
                students.append(f"{roll},{name},{marks}\n")

        with open("students.txt", "w") as file:
            file.writelines(students)

        if deleted:
            print("✅ Student deleted successfully!")
        else:
            print("❌ Student not found.")

    except FileNotFoundError:
        print("No data file found.")


def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")



while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")
