import pickle
import tkinter as tk
from tkinter import messagebox

class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id=None):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details
        self.manager_id = manager_id

    # Method to save employee data to a pickle file
    def save_employee(entries):
        # Create an Employee object using the data from entries
        employee = Employee(
            entries['Name'].get(),
            entries['Employee ID'].get(),
            entries['Department'].get(),
            entries['Job Title'].get(),
            entries['Basic Salary'].get(),
            entries['Age'].get(),
            entries['Date of Birth'].get(),
            entries['Passport Details'].get(),
            entries['Manager ID'].get()
        )

        try:
            # Open the pickle file in append binary mode and dump the employee object
            with open("employee_file.pkl", "ab") as file:
                pickle.dump(employee.__dict__, file)
                return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure

    # Static method to read employee data from the pickle file
    @staticmethod
    def read_employees():
        employees = []  # Initialize an empty list to store employee data
        try:
            # Open the pickle file in read binary mode
            with open("employee_file.pkl", "rb") as file:
                while True:
                    try:
                        employee_data = pickle.load(file)  # Load employee data from the file
                        employees.append(employee_data)  # Append employee data to the list
                    except EOFError:
                        break  # Exit loop when end of file is reached
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
        return employees  # Return the list of employee data

    # Static method to delete an employee from the pickle file based on employee ID
    @staticmethod
    def delete_employee(employee_id):
        try:
            employees = []  # Initialize an empty list to store updated employee data
            # Read existing employees from file
            with open("employee_file.pkl", "rb") as file:
                while True:
                    try:
                        employee = pickle.load(file)  # Load employee data from the file
                        if employee['employee_id'] != employee_id:
                            employees.append(employee)  # Append employee data to the list if ID doesn't match
                    except EOFError:
                        break  # Exit loop when end of file is reached

            # Write back the employees excluding the one to be deleted
            with open("employee_file.pkl", "wb") as file:
                for employee in employees:
                    pickle.dump(employee, file)  # Write updated employee data back to the file
            return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure

    # Static method to check if an employee with the given ID exists
    @staticmethod
    def employee_exists(employee_id):
        employees = Employee.read_employees()  # Read employee data from the pickle file
        for employee in employees:
            if employee.get('employee_id') == employee_id:
                return True  # Return True if employee with given ID exists
        return False  # Return False if employee with given ID doesn't exist

    # Static method to get employee data based on employee ID
    @staticmethod
    def get_employee(employee_id):
        employees = Employee.read_employees()  # Read employee data from the pickle file
        for employee in employees:
            if employee['employee_id'] == employee_id:
                return employee  # Return employee data if found
        return None  # Return None if employee with given ID doesn't exist

    # Static method to modify employee data based on employee ID and new data
    @staticmethod
    def modify_employee(employee_id, new_data):
        try:
            employees = []  # Initialize an empty list to store updated employee data
            with open("employee_file.pkl", "rb") as file:
                while True:
                    try:
                        employee = pickle.load(file)  # Load employee data from the file
                        if employee['employee_id'] == employee_id:
                            employee.update(new_data)  # Update employee data with new data
                        employees.append(employee)  # Append employee data to the list
                    except EOFError:
                        break  # Exit loop when end of file is reached

            with open("employee_file.pkl", "wb") as file:
                for employee in employees:
                    pickle.dump(employee, file)  # Write updated employee data back to the file
            return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure
