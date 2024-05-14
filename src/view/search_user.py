from datetime import date

import sys
sys.path.append("src")

import model.Payroll_Logic as Payroll_Logic
import controller.usercontroller as usercontroller
from model.Payroll_Logic import *
from controller.usercontroller import *

try:
    idnumber = input("Enter the ID of the user you want to search: ")
    searched_user = usercontroller.SearchById(idnumber)
    print (f"User found: {searched_user.firstname} {searched_user.surname}")

except Exception as err:
    print ("Error: ")
    print (str(err))