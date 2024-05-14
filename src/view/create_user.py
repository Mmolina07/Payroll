from datetime import date

import sys
sys.path.append("src")

import model.Payroll_Logic as Payroll_Logic
import controller.usercontroller as usercontroller
from model.Payroll_Logic import *
from controller.usercontroller import *


user_test = Employee( "", "", "", "")

user_test.firstname =firstname = str(input("Enter your  first name: "))
user_test.surname = str(input("Enter your first surname: "))
user_test.idnumber = str(input("Enter your number of ID: "))
user_test.mail = str(input("Enter your mail: "))
usercontroller.Insert(user_test)
print("User successfully inserted")


#CreateAccrualsTable()
#test_accruals = Accruals("2300000", "1", "1", "1", "1", "0", "0", "0", "0")
#InsertAccruals(test_accruals)
#test_Deductions = Deductions("1","1","1","1")
#InsertDeductions(test_Deductions)
#CreateTableDeductions()