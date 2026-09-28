    
# 
#        OFFICE MANAGEMENT SYSTEM
# 
# This program is made for managing basic
# information of employees in an office. 

import os


# Function to add a new employee
def add_employee():

    print("\n ADD EMPLOYEE ")

    emp_id = input("Enter employee ID: ")

    file = open("employees.txt", "a")

    name = input("Enter employee name: ")
    age = input("Enter age: ")
    department = input("Enter department: ")
    designation = input("Enter designation: ")
    phone = input("Enter phone number: ")
    salary = input("Enter monthly salary: ")

    data = emp_id + "|" + name + "|" + age + "|" + department + "|" + designation + "|" + phone + "|" + salary + "\n"

    file.write(data)
    file.close()

    print("Employee added successfully.")


# Function to display all employees
def display_employees():

    print("\n EMPLOYEE DETAILS ")

    try:
        file = open("employees.txt", "r")

        lines = file.readlines()

        if len(lines) == 0:
            print("No employee records available.")

        else:
            for line in lines:

                data = line.strip().split("|")

                if len(data) == 7:
                    print("")
                    print("Employee ID :", data[0])
                    print("Name        :", data[1])
                    print("Age         :", data[2])
                    print("Department  :", data[3])
                    print("Designation :", data[4])
                    print("Phone       :", data[5])
                    print("Salary      :", data[6])

        file.close()

    except FileNotFoundError:
        print("No employee file found.")


# Function to search employee
def search_employee():

    print("\n SEARCH EMPLOYEE ")

    search_id = input("Enter employee ID: ")

    found = False

    try:
        file = open("employees.txt", "r")

        for line in file:

            data = line.strip().split("|")

            if len(data) == 7:

                if data[0] == search_id:

                    print("\nEmployee found!")
                    print("")
                    print("Employee ID :", data[0])
                    print("Name        :", data[1])
                    print("Age         :", data[2])
                    print("Department  :", data[3])
                    print("Designation :", data[4])
                    print("Phone       :", data[5])
                    print("Salary      :", data[6])

                    found = True
                    break

        file.close()

        if found == False:
            print("Employee not found.")

    except FileNotFoundError:
        print("Employee file does not exist.")


# Function to update employee
def update_employee():

    print("\n UPDATE EMPLOYEE ")

    update_id = input("Enter employee ID: ")

    try:
        file = open("employees.txt", "r")

        lines = file.readlines()
        file.close()

        found = False
        new_lines = []

        for line in lines:

            data = line.strip().split("|")

            if len(data) == 7 and data[0] == update_id:

                found = True

                print("Enter new details.")

                name = input("Enter new name: ")
                age = input("Enter new age: ")
                department = input("Enter new department: ")
                designation = input("Enter new designation: ")
                phone = input("Enter new phone number: ")
                salary = input("Enter new salary: ")

                new_data = update_id + "|" + name + "|" + age + "|" + department + "|" + designation + "|" + phone + "|" + salary + "\n"

                new_lines.append(new_data)

            else:
                new_lines.append(line)

        if found:

            file = open("employees.txt", "w")

            for line in new_lines:
                file.write(line)

            file.close()

            print("Employee details updated.")

        else:
            print("Employee ID not found.")

    except FileNotFoundError:
        print("Employee file does not exist.")


# Function to delete employee
def delete_employee():

    print("\n DELETE EMPLOYEE ")

    delete_id = input("Enter employee ID: ")

    try:
        file = open("employees.txt", "r")

        lines = file.readlines()

        file.close()

        found = False
        new_lines = []

        for line in lines:

            data = line.strip().split("|")

            if len(data) == 7 and data[0] == delete_id:
                found = True
            else:
                new_lines.append(line)

        if found:

            file = open("employees.txt", "w")

            for line in new_lines:
                file.write(line)

            file.close()

            print("Employee deleted successfully.")

        else:
            print("Employee ID not found.")

    except FileNotFoundError:
        print("Employee file does not exist.")


# Function for attendance
def mark_attendance():

    print("\n ATTENDANCE ")

    emp_id = input("Enter employee ID: ")
    date = input("Enter date (DD/MM/YYYY): ")
    status = input("Enter Present or Absent: ")

    file = open("attendance.txt", "a")

    data = emp_id + "|" + date + "|" + status + "\n"

    file.write(data)
    file.close()

    print("Attendance recorded.")


# Function to display attendance
def display_attendance():

    print("\n ATTENDANCE RECORD ")

    try:
        file = open("attendance.txt", "r")

        lines = file.readlines()

        if len(lines) == 0:
            print("No attendance records.")

        else:

            for line in lines:

                data = line.strip().split("|")

                if len(data) == 3:

                    print("")
                    print("Employee ID :", data[0])
                    print("Date        :", data[1])
                    print("Status      :", data[2])

        file.close()

    except FileNotFoundError:
        print("No attendance file found.")


# Function to apply leave
def apply_leave():

    print("\n APPLY FOR LEAVE ")

    emp_id = input("Enter employee ID: ")
    leave_type = input("Enter leave type: ")
    days = input("Enter number of days: ")
    reason = input("Enter reason: ")

    file = open("leaves.txt", "a")

    data = emp_id + "|" + leave_type + "|" + days + "|" + reason + "|Pending\n"

    file.write(data)
    file.close()

    print("Leave application submitted.")


# Function to display leaves
def display_leaves():

    print("\n LEAVE RECORDS ")

    try:
        file = open("leaves.txt", "r")

        lines = file.readlines()

        if len(lines) == 0:
            print("No leave applications found.")

        else:

            for line in lines:

                data = line.strip().split("|")

                if len(data) == 5:

                    print("")
                    print("Employee ID :", data[0])
                    print("Leave Type  :", data[1])
                    print("Days        :", data[2])
                    print("Reason      :", data[3])
                    print("Status      :", data[4])

        file.close()

    except FileNotFoundError:
        print("No leave file found.")


# Function to display salary
def salary_details():

    print("\n SALARY DETAILS ")

    emp_id = input("Enter employee ID: ")

    try:
        file = open("employees.txt", "r")

        found = False

        for line in file:

            data = line.strip().split("|")

            if len(data) == 7 and data[0] == emp_id:

                found = True

                print("")
                print("Employee ID :", data[0])
                print("Name        :", data[1])
                print("Department  :", data[3])
                print("Designation :", data[4])
                print("Monthly Salary :", data[6])

                try:
                    salary = float(data[6])
                    yearly = salary * 12
                    print("Yearly Salary  :", yearly)

                except ValueError:
                    print("Salary value is not a number.")

                break

        file.close()

        if found == False:
            print("Employee not found.")

    except FileNotFoundError:
        print("Employee file does not exist.")


# Function to count employees
def employee_count():

    print("\n EMPLOYEE COUNT ")

    try:
        file = open("employees.txt", "r")

        count = 0

        for line in file:

            data = line.strip().split("|")

            if len(data) == 7:
                count = count + 1

        file.close()

        print("Total number of employees:", count)

    except FileNotFoundError:
        print("Total number of employees: 0")


# Function to search department
def department_search():

    print("\n DEPARTMENT SEARCH ")

    department = input("Enter department name: ")

    found = False

    try:
        file = open("employees.txt", "r")

        for line in file:

            data = line.strip().split("|")

            if len(data) == 7:

                if data[3].lower() == department.lower():

                    print("")
                    print("Employee ID :", data[0])
                    print("Name        :", data[1])
                    print("Designation :", data[4])

                    found = True

        file.close()

        if found == False:
            print("No employee found in this department.")

    except FileNotFoundError:
        print("Employee file does not exist.")


# Main menu
while True:

    print("\n")
    print("OFFICE MANAGEMENT SYSTEM")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Mark Attendance")
    print("7. Display Attendance")
    print("8. Apply for Leave")
    print("9. Display Leave Details")
    print("10. Salary Details")
    print("11. Department Search")
    print("12. Employee Count")
    print("13. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        display_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        mark_attendance()

    elif choice == "7":
        display_attendance()

    elif choice == "8":
        apply_leave()

    elif choice == "9":
        display_leaves()

    elif choice == "10":
        salary_details()

    elif choice == "11":
        department_search()

    elif choice == "12":
        employee_count()

    elif choice == "13":

        print("\nThank you for using the Office Management System.")
        print("Program ended.")

        break

    else:

        print("\nWrong choice.")
        print("Please enter a number from 1 to 13.")
      
