from datetime import date

import sys
sys.path.append("src")

import model.Payroll_Logic as Payroll_Logic
import controller.usercontroller as usercontroller
from model.Payroll_Logic import *
from controller.usercontroller import *

def menu():
    while True:
        print("\n--- Table Modification Menu ---")
        print("1. Create 'employees' table ")
        print("2. Create 'Deductions' table ")
        print("3. Create 'Accruals' table ")
        print("4. Delete 'employees' table ")
        print("5. Delete 'Deductions' table ")
        print("6. Delete 'Accruals' table ")
        print("7. Close")
        choice = input("Select an option: ")

        if choice == '1':
            CreateTable()
        elif choice == '2':
            CreateTableDeductions()
        elif choice == '3':
            CreateAccrualsTable()
        elif choice == '4':
            DeleteTable()
        elif choice == '5':
            DeleteTableDeductions()
        elif choice == '6':
            DeleteTableAccruals()
        elif choice == '7':
            print("Leaving the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
