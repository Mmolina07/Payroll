"""User interface that prompts for the input data required to calculate the employee's payroll."""

"""All methods of the Payroll Logic module are imported"""

import sys

sys.path.append("src")

from logic.Payroll_Logic import *


def main():

    print("This program allows you to calculate the payroll accounting.")
    BasicSalary = float(input("Enter the monthly base salary: "))
    TransportSubsidy = float(input("Enter the transportation subsidy: "))
    WorkedDays = int(input("Enter the days worked (15 or 30): "))
    HolidayTimeWorked = int(input("Enter the holidays worked: "))
    ExtraDaylightHoursWorked = int(input("Enter the number of daylight extra hours worked: "))
    ExtraNightHoursWorked = int(input("Enter the number of night extra hours worked: "))
    HolidayExtraDaylightHoursWorked = int(input("Enter the number of holiday daylight extra hours worked: "))
    HolidayExtraNightHoursWorked = int(input("Enter the number of holiday night extra hours worked: "))
    HealthInsurancePercentage = float(input("Enter the health contribution percentage: "))
    PensionContributionPercentage = float(input("Enter the pension contribution percentage: "))
    PensionSolidarityFundContributionPercentage = float(input("Enter the percentage of pension solidarity fund contribution: "))
    DaysOfDisability = int(input("Enter the number of days of disability:"))
    LeaveDays = int(input("Enter the number of leave days: "))

    CalculatePayrollPaymentCallingAllFunctions(BasicSalary, TransportSubsidy, WorkedDays, HolidayTimeWorked, ExtraDaylightHoursWorked, 
    ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked, HolidayExtraNightHoursWorked, HealthInsurancePercentage, 
    PensionContributionPercentage, PensionSolidarityFundContributionPercentage, DaysOfDisability, LeaveDays, CalculateWithholdingTax)
main()

