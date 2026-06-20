students = []

while True:

    print("1. Add Student")
    print("2. View Student")
    print("3. search Student")
    print("4. Delete Student")
    print("5.Exit")
    

    choice = input("Enter your choice: ")

  # Add Student
    if choice == "1":
        name = input("Enter your Student name: ")
        students.append(name)
        print(students)

        # View Students
    elif choice == "2":
        for student in students:
          print(student)
        
    # Search Student
    elif choice=="3":
        search_name=input("enter student name to search")

        if search_name in students:
            print("student found")
        else:
            print("student not found")

            # Delete Student
    elif choice == "4":
        delete = input("Enter student name to delete: ")
        if delete in students:
            students.remove(delete)
            print("Student deleted successfully!")
        else:
            print("Student not found!")

            # Exit
    elif choice == "5":
        print("Program closed")
        break

    else:
        print("Invalid choice!")
 

          