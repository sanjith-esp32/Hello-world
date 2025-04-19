# Simple Employee Management System

employees = {}

def add_employee(emp_id, name, position):
    if emp_id in employees:
        print(f"Employee with ID {emp_id} already exists.")
    else:
        employees[emp_id] = {"name": name, "position": position}
        print(f"Employee {name} added successfully.")

def remove_employee(emp_id):
    if emp_id in employees:
        removed_employee = employees.pop(emp_id)
        print(f"Employee {removed_employee['name']} removed successfully.")
    else:
        print(f"Employee with ID {emp_id} does not exist.")

def update_employee(emp_id, name=None, position=None):
    if emp_id in employees:
        if name:
            employees[emp_id]["name"] = name
        if position:
            employees[emp_id]["position"] = position
        print(f"Employee with ID {emp_id} updated successfully.")
    else:
        print(f"Employee with ID {emp_id} does not exist.")

def view_employees():
    if employees:
        print("\nEmployee List:")
        for emp_id, details in employees.items():
            print(f"ID: {emp_id}, Name: {details['name']}, Position: {details['position']}")
    else:
        print("No employees found.")

# Main menu
while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Update Employee")
    print("4. View Employees")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        position = input("Enter Employee Position: ")
        add_employee(emp_id, name, position)
    elif choice == "2":
        emp_id = input("Enter Employee ID to remove: ")
        remove_employee(emp_id)
    elif choice == "3":
        emp_id = input("Enter Employee ID to update: ")
        name = input("Enter new name (leave blank to skip): ")
        position = input("Enter new position (leave blank to skip): ")
        update_employee(emp_id, name if name else None, position if position else None)
    elif choice == "4":
        view_employees()
    elif choice == "5":
        print("Exiting Employee Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")