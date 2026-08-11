students_list = []


def get_student_input():
    while True:
        st_name = input("Enter Student Name: ").strip()
        if st_name:
            break
        else:
            print("Name cannot be empty!")

    while True:
        roll_number = input("Enter Roll Number: ").strip()
        if not roll_number:
            print("Roll Number cannot be empty!")
            continue

        found = False
        for student in students_list:
            if student["roll_number"] == roll_number:
                found = True
                break

        if found:
            print("Roll Number already exists. Enter another one.")
        else:
            break

    while True:
        try:
            age = int(input("Enter Age: "))
            if age <= 0:
                print("Please enter a valid positive age.")
                continue
            break
        except ValueError:
            print("Please enter age in numbers only.")

    while True:
        course = input("Enter Course: ").strip()
        if course:
            break
        else:
            print("Course cannot be empty!")

    return st_name, roll_number, age, course


def add_student(st_name, roll_number, age, course):
    student_dict = {
        "name": st_name,
        "roll_number": roll_number,
        "age": age,
        "course": course
    }
    students_list.append(student_dict)
    print(f"\nStudent '{st_name}' added successfully!")


def display_students():
    if not students_list:
        print("\nNo students found.")
        return

    print("\n===== Student List =====")
    for student in students_list:
        print("Name        :", student["name"])
        print("Roll Number :", student["roll_number"])
        print("Age         :", student["age"])
        print("Course      :", student["course"])
        print("-" * 30)

    print("Total Students:", len(students_list))


def search_student(roll_number):
    for student in students_list:
        if student["roll_number"] == roll_number:
            print("\nStudent Found:")
            print("Name        :", student["name"])
            print("Roll Number :", student["roll_number"])
            print("Age         :", student["age"])
            print("Course      :", student["course"])
            return

    print("Student not found.")


def update_student(roll_number):
    for student in students_list:
        if student["roll_number"] == roll_number:
            new_name = input("Enter New Name (leave blank to keep current): ").strip()
            if new_name:
                student["name"] = new_name

            while True:
                age_input = input("Enter New Age (leave blank to keep current): ").strip()
                if not age_input:
                    break
                try:
                    new_age = int(age_input)
                    if new_age > 0:
                        student["age"] = new_age
                        break
                    else:
                        print("Age must be positive.")
                except ValueError:
                    print("Enter age in numbers only.")

            new_course = input("Enter New Course (leave blank to keep current): ").strip()
            if new_course:
                student["course"] = new_course

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student(roll_number):
    for student in students_list:
        if student["roll_number"] == roll_number:
            students_list.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# Main Program Loop
if __name__ == "__main__":
    while True:
        print("\n===== Student Record Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            st_name, roll_number, age, course = get_student_input()
            add_student(st_name, roll_number, age, course)

        elif choice == "2":
            display_students()

        elif choice == "3":
            roll_number = input("Enter Roll Number to Search: ").strip()
            search_student(roll_number)

        elif choice == "4":
            roll_number = input("Enter Roll Number to Update: ").strip()
            update_student(roll_number)

        elif choice == "5":
            roll_number = input("Enter Roll Number to Delete: ").strip()
            delete_student(roll_number)

        elif choice == "6":
            print("Exiting")
            break

        else:
            print("Invalid choice! Please try again.")
