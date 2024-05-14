from datetime import date

import sys
sys.path.append("src")

import model.Payroll_Logic as Payroll_Logic
import controller.usercontroller as usercontroller
from model.Payroll_Logic import *
from controller.usercontroller import *


try:
    idnumber = input("Enter the ID of the user you want to change any info: ")
    employee = SearchById(idnumber)

    if employee is not None:
        print(f"Employee found: {employee.firstname} {employee.surname}, ID: {employee.idnumber}, Email: {employee.mail}")
        
        valid_field = False
        while not valid_field:
            field_to_change = input("Which info would you like to change? (firstname, surname, mail): ")

            if field_to_change in ['firstname', 'surname', 'mail']:
                valid_field = True
                new_value = input(f"Enter the new value for {field_to_change}: ")
                
                setattr(employee, field_to_change, new_value)
                
                Update(employee)

                print(f"{field_to_change} changed succesfully")
            else:
                print("Invalid field. Please enter either 'firstname', 'surname', or 'mail'.")
    else:
        print("Employee not found.")

except ErrorNotfound as e:
    print(e)
