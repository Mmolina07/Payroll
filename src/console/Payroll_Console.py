"""User interface that prompts for the input data required to calculate the employee's payroll."""

"""All methods of the Payroll Logic module are imported"""

import sys

sys.path.append("src")

from logic.Payroll_Logic import *


def main():
    print("This program allows you to calculate the payroll accounting.")
    
    while True:
        try:
            BasicSalary = float(input("Enter the monthly base salary: "))
            if BasicSalary < 30000:
                raise ValueError("The base salary cannot be less than 30000.")
            break
        except ValueError as ve:
            if "could not convert string to float" in str(ve):
                print("Error: Por favor, ingresa un número válido.")
            else:
                print("Error: " + str(ve))

    while True:
        try:
            WorkedDays = int(input("Enter the days worked (15 or 30): "))
            if WorkedDays > 30:
                raise ValueError("it may be less than 30 days to make the payroll process.")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10:" in str(ve):
                print("Error: invalid value for worked days, please correct it.")
            else:
                print("Error: " + str(ve))

    while True:
        try:
            HolidayTimeWorked = int(input("Enter the holidays worked: "))
            if HolidayTimeWorked > 3:
                raise ValueError("3 days cannot be exceeded for the payroll process.")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10:" in str(ve):
                print("Error: invalid value for Holiday time worked, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            ExtraDaylightHoursWorked = int(input("Enter the number of daylight extra hours worked: "))
            if ExtraDaylightHoursWorked > 12:
                raise ValueError("12 days cannot be exceeded for the payroll process.")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10:" in str(ve):
                print("Error: invalid value for Daylight hours worked, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            ExtraNightHoursWorked = int(input("Enter the number of night extra hours worked: "))
            if ExtraNightHoursWorked > 12:
                raise ValueError("12 days cannot be exceeded for the payroll process.")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10:" in str(ve):
                print("Error: invalid value for night worked hours, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            HolidayExtraDaylightHoursWorked = int(input("Enter the number of holiday daylight extra hours worked: "))
            if HolidayExtraDaylightHoursWorked > 12:
                raise ValueError("12 days cannot be exceeded for the payroll process.")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10:" in str(ve):
                print("Error: invalid value for Holiday Daylight hours worked, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            HolidayExtraNightHoursWorked = int(input("Enter the number of holiday night extra hours worked: "))
            if HolidayExtraNightHoursWorked > 12:
                raise ValueError("12 days cannot be exceeded for the payroll process.")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10:" in str(ve):
                print("Error: invalid value for Holiday night worked hours, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            HealthInsurancePercentage = float(input("Enter the health contribution percentage: "))
            if HealthInsurancePercentage > 4:
                raise ValueError("4% cannot be exceeded for the payroll process")
            break
        except ValueError as ve:
            if "could not convert string to float" in str(ve):
                print("Error: invalid value for health percentage, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            PensionContributionPercentage = float(input("Enter the pension contribution percentage: "))
            if PensionContributionPercentage > 4:
                raise ValueError("4% cannot be exceeded for the payroll process")
            break
        except ValueError as ve:
            if "could not convert string to float" in str(ve):
                print("Error: invalid value for pension contribution, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            PensionSolidarityFundContributionPercentage = float(input("Enter the percentage of pension solidarity fund contribution: "))
            if PensionSolidarityFundContributionPercentage > 3:
                raise ValueError("3% cannot be exceeded for the payroll process")
            break
        except ValueError as ve:
            if "could not convert string to float" in str(ve):
                print("Error: invalid value for pension solidarity fund, please correct it.")
            else:
                print("Error: " + str(ve))
    
    while True:
        try:
            DaysOfDisability = int(input("Enter the number of days of disability:"))
            if DaysOfDisability > 30:
                raise ValueError("30 days cannot be exceeded for the payroll process")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10:" in str(ve):
                print("Error: invalid value for days of disability, please correct it")
            else:
                print("Error: " + str(ve))    
    
    while True:
        try:
            LeaveDays = int(input("Enter the number of leave days: "))
            if LeaveDays > 30:
                raise ValueError("30 days cannot be exceeded for the payroll process")
            break
        except ValueError as ve:
            if "invalid literal for int() with base 10" in str(ve):
                print("Error: invalid value for leave days, please correct it")
            else:
                print("Error: " + str(ve))
    
    # Crea una instancia de la clase Accruals
    accruals = Accruals(BasicSalary, WorkedDays, HolidayTimeWorked, ExtraDaylightHoursWorked,
                        ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked,
                        HolidayExtraNightHoursWorked)

    # Crea una instancia de la clase Deductions
    deductions = Deductions(accruals, HealthInsurancePercentage, PensionContributionPercentage, 
                            PensionSolidarityFundContributionPercentage, DaysOfDisability, LeaveDays)

    # Crea una instancia de la clase SalaryCalculator
    calculator = SalaryCalculator(accruals, deductions)

    print("Net salary:", calculator.calculate_net_salary())

if __name__ == "__main__":
    main()



