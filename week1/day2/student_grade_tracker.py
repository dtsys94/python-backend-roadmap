students = []

def show_menu():
    print("\n---Student Grade Tracker---")
    print("1. Add student")
    print("2. View Students")
    print("3. Find Student")
    print("4. Quit")

while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter the student name ")
        grade = int(input("Enter the student grade "))
        student = {
            "name": name,
            "grade": grade
        }
        students.append(student)
        print(f"{name} added successfully")
    

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print(f"{student['name']} - {student['grade']}")

    elif choice == "3":
        found = False
    
        find_name = input("What is the student`s name? ")
        for student in students:
            if student["name"] == find_name:
                found = True
                print(f"{student['name']}-{student['grade']}")
        if not found:
            print("Student not found")
        
    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid choice")