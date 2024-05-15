from datetime import date

import sys
sys.path.append("src")

import model.Payroll_Logic as Payroll_Logic
import controller.usercontroller as usercontroller
from model.Payroll_Logic import *
from controller.usercontroller import *

def input_employee():
    firstname = input("Enter first name: ")
    surname = input("Enter surname: ")
    idnumber = input("Enter ID number: ")
    mail = input("Enter email: ")
    return Employee(firstname, surname, idnumber, mail)

def input_accruals():
    idnumber = input("Type your id number: ")
    BasicSalary = input("Enter basic salary: ")
    WorkedDays = input("Enter worked days: ")
    HolidayTimeWorked = input("Enter holiday time worked: ")
    ExtraDaylightHoursWorked = input("Enter extra daylight hours worked: ")
    ExtraNightHoursWorked = input("Enter extra night hours worked: ")
    HolidayExtraDaylightHoursWorked = input("Enter holiday extra daylight hours worked: ")
    HolidayExtraNightHoursWorked = input("Enter holiday extra night hours worked: ")
    DaysOfDisability = input("Enter days of disability: ")
    LeaveDays = input("Enter leave days: ")
    return Accruals(idnumber, BasicSalary, WorkedDays, HolidayTimeWorked,
    ExtraDaylightHoursWorked, ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked,
    HolidayExtraNightHoursWorked, DaysOfDisability, LeaveDays)

def input_deductions():
    idnumber = input("Type your id number: ")
    accruals = Accruals
    HealthInsurancePercentage = input("Enter health insurance percentage: ")
    PensionContributionPercentage = input("Enter pension contribution percentage: ")
    PensionSolidarityFundContributionPercentage = input("Enter pension solidarity fund contribution percentage: ")
    return Deductions(idnumber, accruals, HealthInsurancePercentage, PensionContributionPercentage,
                    PensionSolidarityFundContributionPercentage)

def menu():
    while True:
        print("\n--- Information Insertion Menu ---")
        print("1. Insert information into 'employees' table")
        print("2. Insert information into 'accruals' table")
        print("3. Insert information into 'deductions' table")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            employee = input_employee()
            try:
                Insert(employee)
                print("Employee inserted successfully.")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inserting employee: {e}")
        elif choice == '2':
            accruals = input_accruals()
            try:
                InsertAccruals(accruals)
                print("Accruals information inserted successfully.")
            except Exception as e:
                print(f"Error inserting accruals information: {e}")
        elif choice == '3':
            deductions = input_deductions()
            try:
                InsertDeductions(deductions)
                print("Deductions information inserted successfully.")
            except Exception as e:
                print(f"Error inserting deductions information: {e}")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()