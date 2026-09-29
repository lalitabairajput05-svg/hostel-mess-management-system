# Hostel Mess Management System

def add_student():
    room = input("Enter room number: ")
    name = input("Enter student name: ")
    m_type = input("Enter mess type (Veg/Non-Veg): ")

    # check if room already exists
    try:
        f = open("mess_records.txt", "r")
        for line in f:
            row = line.strip().split(",")
            if row[0] == room:
                print("Student with this room number already exists!")
                f.close()
                return
        f.close()
    except:
        pass

    f = open("mess_records.txt", "a")
    f.write(room + "," + name + "," + m_type + ",0\n")
    f.close()
    print("Student added successfully!")


def view_students():
    try:
        f = open("mess_records.txt", "r")
    except:
        print("No records found!")
        return

    print("\n--- Hostel Student Details ---")
    print("----------------------------------------")
    for line in f:
        row = line.strip().split(",")
        print("Room Number :", row[0])
        print("Name        :", row[1])
        print("Mess Type   :", row[2])
        print("Meals Taken :", row[3])
        print("----------------------------------------")
    f.close()


def mark_meal():
    try:
        f = open("mess_records.txt", "r")
        students = []
        for line in f:
            students.append(line.strip().split(","))
        f.close()
    except:
        print("No student records found!")
        return

    if len(students) == 0:
        print("No students in file.")
        return

    room = input("Enter room number: ")
    found = 0

    for s in students:
        if s[0] == room:
            s[3] = str(int(s[3]) + 1)
            found = 1
            print("Meal marked successfully for", s[1])
            break

    if found == 1:
        f = open("mess_records.txt", "w")
        for s in students:
            f.write(s[0] + "," + s[1] + "," + s[2] + "," + s[3] + "\n")
        f.close()
    else:
        print("Student not found!")


def search_student():
    room = input("Enter room number to search: ")

    try:
        f = open("mess_records.txt", "r")
    except:
        print("No records found!")
        return

    found = 0
    for line in f:
        row = line.strip().split(",")
        if row[0] == room:
            print("\n--- Student Details ---")
            print("Room Number :", row[0])
            print("Name        :", row[1])
            print("Mess Type   :", row[2])
            print("Meals Taken :", row[3])
            found = 1
            break
    f.close()

    if found == 0:
        print("Student not found!")


def calculate_bill():
    room = input("Enter room number: ")

    try:
        f = open("mess_records.txt", "r")
    except:
        print("No records found!")
        return

    found = 0
    for line in f:
        row = line.strip().split(",")
        if row[0] == room:
            meals = int(row[3])
            cost = 60
            total = meals * cost

            print("\n--- Mess Bill ---")
            print("Student Name :", row[1])
            print("Room Number  :", row[0])
            print("Mess Type    :", row[2])
            print("Meals Taken  :", meals)
            print("Meal Cost    : Rs.", cost)
            print("Total Bill   : Rs.", total)
            found = 1
            break
    f.close()

    if found == 0:
        print("Student not found!")


def main():
    while True:
        print("\n--- HOSTEL MESS MANAGEMENT ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Mark Meal")
        print("4. Search Student")
        print("5. Calculate Mess Bill")
        print("6. Exit")

        ch = input("Enter choice (1-6): ")

        if ch == "1":
            add_student()
        elif ch == "2":
            view_students()
        elif ch == "3":
            mark_meal()
        elif ch == "4":
            search_student()
        elif ch == "5":
            calculate_bill()
        elif ch == "6":
            print("Exiting system. Thank you!")
            break
        else:
            print("Invalid choice, try again.")


main()
