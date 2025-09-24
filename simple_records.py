def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")
    student = {"Name": name, "Age": age, "Course": course}
    students.append(student)
    print("✅ Student added successfully!\n")

def view_students():
    if not students:
        print("⚠️ No student records found.\n")
    else:
        print("\n--- All Student Records ---")
        for i, student in enumerate(students, start=1):
            print(f"{i}. Name: {student['Name']}, Age: {student['Age']}, Course: {student['Course']}")
        print()

def search_student():
    search_name = input("Enter student name to search: ")
    found = False
    for student in students:
        if student["Name"].lower() == search_name.lower():
            print(f"\n✅ Student Found: Name: {student['Name']}, Age: {student['Age']}, Course: {student['Course']}\n")
            found = True
            break
    if not found:
        print("⚠️ Student not found.\n")

def menu():
    while True:
        print("=== Simple Student Record System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please try again.\n")

menu()
