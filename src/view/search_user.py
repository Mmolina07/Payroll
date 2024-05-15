import psycopg2
import sys
sys.path.append("src")
import controller.SecretConfig as SecretConfig
from model.Payroll_Logic import *
import controller.usercontroller as usercontroller

def search_by_id():
    try:
        idnumber = input("Enter the ID of the user you want to search: ")
        searched_user = usercontroller.SearchById(idnumber)
        print(f"User found: {searched_user.firstname} {searched_user.surname} {searched_user.idnumber} {searched_user.mail}")
    except Exception as err:
        print("Error:", err)

def search_by_id_tables():
    try:
        idnumber = input("Enter the ID of the user you want to search: ")
        searched_user = usercontroller.SearchInAllTablesByID(idnumber)
        print(f"User found: {searched_user.firstname} {searched_user.surname} {searched_user.idnumber} {searched_user.mail}")
    except Exception as err:
        print("Error:", err)

def search_by_name_surname():
    try:
        firstname = input("Enter the first name: ")
        surname = input("Enter the surname: ")
        searched_user = usercontroller.SearchByNameAndSurname(firstname, surname)
        if searched_user:
            print(f"User found: {searched_user.firstname} {searched_user.surname} {searched_user.idnumber} {searched_user.mail}")
        else:
            print("User not found.")
    except Exception as err:
        print("Error:", err)

def search_by_id_tables():
    try:
        idnumber = input("Enter the ID of the user you want to search: ")
        result = usercontroller.SearchInAllTablesByID(idnumber)
        employee, accruals, deductions = result

        print(f"Name: {employee.firstname}")
        print(f"Username: {employee.surname}")
        print(f"ID: {employee.idnumber}")
        print(f"Mail: {employee.mail}")


        print(f"Basic salary: {accruals.BasicSalary}")
        print(f"Worked days: {accruals.WorkedDays} for the value of {accruals.CalculateDailySalary()}")
        print(f"Holiday time worked: {accruals.HolidayTimeWorked} for the value of {accruals.CalculateValueOfHolidaysWorked(accruals.CalculateDailySalary())}")
        print(f"Extra daylight hours worked: {accruals.ExtraDaylightHoursWorked} for the value of {accruals.CalculateDaylightExtraHoursCharge()}")
        print(f"Extra night hours worked: {accruals.ExtraNightHoursWorked} for the value of {accruals.CalculateExtraNightHoursCharge()}")
        print(f"Holiday extra daylight hours worked: {accruals.HolidayExtraDaylightHoursWorked} for the value of {accruals.CalculateHolidayExtraDaylightHoursWorkedValue()}")
        print(f"Holiday extra night hours worked: {accruals.HolidayExtraNightHoursWorked} for the value of {accruals.CalculateHolidayExtraNightHoursWorkedValue()}")
        print(f"Days of disability: {accruals.DaysOfDisability} with a value of {accruals.CalculateDisabilityTimeValue()}")
        print(f"Leave days: {accruals.LeaveDays} with a value of {accruals.CalculateLeaveDaysValue()}")

        
        print(f"Health insurance percentage: {deductions.HealthInsurancePercentage} that costs: {deductions.CalculateHealthInsurance()}")
        print(f"Pension contribution percentage: {deductions.PensionContributionPercentage}")
        print(f"Pension solidarity fund contribution percentage: {deductions.PensionSolidarityFundContributionPercentage} that costs: {deductions.CalculatePensionSolidarityFundContribution()}")

        salary_calculator = SalaryCalculator(accruals, deductions)
        net_salary = salary_calculator.calculate_net_salary()
        print(f"Net salary: {net_salary}")
        
    except Exception as err:
        print("Error:", err)


def main():
    while True:
        print("\nMenu:")
        print("1. Search by ID")
        print("2. Search by Name and Surname")
        print("3. Search in all tables by ID")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_by_id()
        elif choice == "2":
            search_by_name_surname()
        elif choice == "3":
            search_by_id_tables()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
