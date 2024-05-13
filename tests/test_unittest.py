import unittest

import sys
sys.path.append("src")

import model.Payroll_Logic as Payroll_Logic
from model.Payroll_Logic import *

class PayrollTests(unittest.TestCase):

    """1st normal unit test to verify that CalculateDailySalary method works correctly"""
    def testCalculateDailySalary1(self):
        accruals = Accruals(BasicSalary = 2000000, 
        WorkedDays = 30, 
        HolidayTimeWorked = 0, 
        ExtraDaylightHoursWorked = 0, 
        ExtraNightHoursWorked = 0, 
        HolidayExtraDaylightHoursWorked = 0, 
        HolidayExtraNightHoursWorked = 0, 
        DaysOfDisability = 0, 
        LeaveDays = 5)

        Result = accruals.CalculateDailySalary()
        self.assertEqual(round(Result,1), 66666.7)

    """2nd normal unit test to verify that calculate_net_salary works correctly"""
    def testcalculate_net_salary(self):

        accruals = Accruals(BasicSalary = 8000000,
        WorkedDays = 30,
        HolidayTimeWorked = 1,
        ExtraDaylightHoursWorked = 1,
        ExtraNightHoursWorked = 0,
        HolidayExtraDaylightHoursWorked = 0,
        HolidayExtraNightHoursWorked = 0,
        DaysOfDisability = 0,
        LeaveDays = 1)

        deductions = Deductions(accruals, HealthInsurancePercentage = 4,
        PensionContributionPercentage = 4,
        PensionSolidarityFundContributionPercentage = 2)

        salary_calculator = SalaryCalculator(accruals, deductions)

        Result = salary_calculator.calculate_net_salary() 
        self.assertEqual(round(Result, 1), 36892303.5)

    """3rd normal unit test to verify that HealthInsurance method works correctly"""
    def testCalculateHealthInsurance(self):

        accruals = Accruals(BasicSalary = 7500000,
        WorkedDays=30, 
        HolidayTimeWorked=0, 
        ExtraDaylightHoursWorked=0,
        ExtraNightHoursWorked=0, 
        HolidayExtraDaylightHoursWorked=0, 
        HolidayExtraNightHoursWorked=0, 
        DaysOfDisability=0, 
        LeaveDays=5)

        deductions = Deductions(accruals, 
        HealthInsurancePercentage = 4, 
        PensionContributionPercentage=0,
        PensionSolidarityFundContributionPercentage=0)
    
        Result = deductions.CalculateHealthInsurance()
        self.assertEqual(Result, 300000)

    """4th normal unit test to verify that CalculatePensionContribution method works correctly"""
    def testCalculatePensionContribution(self):

        accruals = Accruals(BasicSalary = 7500000, 
        WorkedDays=30, 
        HolidayTimeWorked=0, 
        ExtraDaylightHoursWorked=0,
        ExtraNightHoursWorked=0, 
        HolidayExtraDaylightHoursWorked=0, 
        HolidayExtraNightHoursWorked=0, 
        DaysOfDisability=0, 
        LeaveDays=5)

        deductions = Deductions(accruals, 
        HealthInsurancePercentage=0,
        PensionContributionPercentage=4,
        PensionSolidarityFundContributionPercentage=0)

        Result = deductions.CalculatePensionContribution()
        self.assertEqual(Result, 300000)

    """5th normal unit test to verify that CalculatePensionSolidarityFundContribution method works correctly"""
    def testCalculatePensionSolidarityFundContribution(self):
        
        accruals = Accruals(BasicSalary = 5000000, 
        WorkedDays=30, 
        HolidayTimeWorked=0, 
        ExtraDaylightHoursWorked=0,
        ExtraNightHoursWorked=0, 
        HolidayExtraDaylightHoursWorked=0, 
        HolidayExtraNightHoursWorked=0,
        DaysOfDisability=0, LeaveDays=5)

        deductions = Deductions(accruals, 
        HealthInsurancePercentage=0, 
        PensionContributionPercentage=0,
        PensionSolidarityFundContributionPercentage=2)

        Result = deductions.CalculatePensionSolidarityFundContribution()
        self.assertEqual(Result, 100000)

    """6th normal unit test to verify that CalculateDisabilityTimeValue method works correctly"""
    def testCalculateDisabilityTimeValue1(self):
        accruals = Accruals(BasicSalary=7000000, 
        WorkedDays=30,
        HolidayTimeWorked=0,
        ExtraDaylightHoursWorked=0,
        ExtraNightHoursWorked=0,
        HolidayExtraDaylightHoursWorked=0, 
        HolidayExtraNightHoursWorked=0, 
        DaysOfDisability=2, 
        LeaveDays=0)

        Result = accruals.CalculateDisabilityTimeValue()
        self.assertEqual(round(Result,1), 311080.0)

    """7th normal unit test to verify the calculation of disability value greater than 90 and less than 540 days."""
    def testCalculateDisabilityTimeValue2(self):
        
        accruals = Accruals(BasicSalary=700000, 
        WorkedDays=30, 
        HolidayTimeWorked=0, 
        ExtraDaylightHoursWorked=0, 
        ExtraNightHoursWorked=0,
        HolidayExtraDaylightHoursWorked=0, 
        HolidayExtraNightHoursWorked=0,
        DaysOfDisability=180, 
        LeaveDays=0)

        Result = accruals.CalculateDisabilityTimeValue()
        self.assertEqual(round(Result,1), 2100000.0)

    """1st exceptional unit test in the case that a person with a high salary also has high deductions"""
    def testCalculatePayrollPayment1(self):

        accruals = Accruals(BasicSalary=20000000, 
        WorkedDays=30, 
        HolidayTimeWorked=0,
        ExtraDaylightHoursWorked=0,
        ExtraNightHoursWorked=0, 
        HolidayExtraDaylightHoursWorked=0, 
        HolidayExtraNightHoursWorked=0, 
        DaysOfDisability=0, 
        LeaveDays=5)

        deductions = Deductions(accruals, 
        HealthInsurancePercentage= 7, 
        PensionContributionPercentage= 8,
        PensionSolidarityFundContributionPercentage= 3)
      
        salary_calculator = SalaryCalculator(accruals, deductions)

        Result = salary_calculator.calculate_net_salary()
        self.assertEqual(round(Result, 1), 12143837.0)

    """2nd exceptional unit test in the case of a high number of days of disability"""
    def testCalculatePayrollPayment2(self):

        accruals = Accruals(BasicSalary=1500000, 
        WorkedDays=10, 
        HolidayTimeWorked=0, 
        ExtraDaylightHoursWorked=0,
        ExtraNightHoursWorked=0, 
        HolidayExtraDaylightHoursWorked=0, 
        HolidayExtraNightHoursWorked=0, 
        DaysOfDisability=20, 
        LeaveDays=5)

        deductions = Deductions(accruals, 
        HealthInsurancePercentage=4, 
        PensionContributionPercentage=4,
        PensionSolidarityFundContributionPercentage=4)
        
        salary_calculator = SalaryCalculator(accruals, deductions)
         
        Result = salary_calculator.calculate_net_salary()
        self.assertEqual(round(Result,1), 1169168)

    """3rd exceptional unit test in the case of a person who started working in the middle of the month"""
    def testCalculatePayrollPayment3(self):
        accruals = Accruals(BasicSalary=4000000, 
        WorkedDays=15, 
        HolidayTimeWorked=0, 
        ExtraDaylightHoursWorked=0,
        ExtraNightHoursWorked=0, 
        HolidayExtraDaylightHoursWorked=0, 
        HolidayExtraNightHoursWorked=0,
        DaysOfDisability=0, 
        LeaveDays=5)

        deductions = Deductions(accruals, 
        HealthInsurancePercentage=4, 
        PensionContributionPercentage=4,
        PensionSolidarityFundContributionPercentage=4)
        
        salary_calculator = SalaryCalculator(accruals, deductions)
         
        Result = salary_calculator.calculate_net_salary()
        self.assertEqual(round(Result, 1), 1760000)

    """4th exceptional unit test in the case of a person worked a lot of extra hours"""
    def testCalculatePayrollPayment4(self):

        accruals = Accruals(BasicSalary = 6000000,
        WorkedDays = 30,
        HolidayTimeWorked = 0,
        ExtraDaylightHoursWorked = 5,
        ExtraNightHoursWorked = 6,
        HolidayExtraDaylightHoursWorked = 5,
        HolidayExtraNightHoursWorked = 5,
        DaysOfDisability = 0,
        LeaveDays = 5)

        deductions = Deductions(accruals, HealthInsurancePercentage = 4,
        PensionContributionPercentage = 4,
        PensionSolidarityFundContributionPercentage = 4)

        salary_calculator = SalaryCalculator(accruals, deductions)

        Result = salary_calculator.calculate_net_salary() 
        self.assertEqual(round(Result, 1 ), 5180598.5)

    """5th exceptional unit test in the case of a high number of leave days"""
    def testCalculatePayrollPayment5(self):
    
        accruals = Accruals(BasicSalary = 2500000,
        WorkedDays = 5,
        HolidayTimeWorked = 0,
        ExtraDaylightHoursWorked = 0,
        ExtraNightHoursWorked = 0,
        HolidayExtraDaylightHoursWorked = 0,
        HolidayExtraNightHoursWorked = 0, 
        DaysOfDisability = 0,
        LeaveDays = 1)

        deductions = Deductions(accruals, 
        HealthInsurancePercentage = 4,
        PensionContributionPercentage = 4,
        PensionSolidarityFundContributionPercentage = 2)

        salary_calculator = SalaryCalculator(accruals, deductions)

        Result = salary_calculator.calculate_net_salary()
        self.assertEqual(round(Result, 1), 9970800.0)

    """6th exceptional unit test in the case of a high number of holidays worked"""
    def testCalculatePayrollPayment6(self):

        accruals = Accruals(BasicSalary = 5000000,
        WorkedDays = 17,
        HolidayTimeWorked = 3,
        ExtraDaylightHoursWorked = 0,
        ExtraNightHoursWorked = 0,
        HolidayExtraDaylightHoursWorked = 7,
        HolidayExtraNightHoursWorked = 6,
        DaysOfDisability = 0,
        LeaveDays = 5)

        deductions = Deductions(accruals, HealthInsurancePercentage = 4,
        PensionContributionPercentage = 4,
        PensionSolidarityFundContributionPercentage = 4)

        salary_calculator = SalaryCalculator(accruals, deductions)

        Result = salary_calculator.calculate_net_salary() 
        self.assertEqual(round(Result, 1 ), 2864033.2)

    """7th exceptional unit test in the case of a person has minimum deductions"""
    def testCalculatePayrollPayment7(self):
        
        accruals = Accruals(BasicSalary = 800000,
        WorkedDays = 30,
        HolidayTimeWorked = 0,
        ExtraDaylightHoursWorked = 0,
        ExtraNightHoursWorked = 0,
        HolidayExtraDaylightHoursWorked = 0,
        HolidayExtraNightHoursWorked = 0,
        DaysOfDisability = 0,
        LeaveDays = 5)

        deductions = Deductions(accruals, HealthInsurancePercentage = 1,
        PensionContributionPercentage = 1,
        PensionSolidarityFundContributionPercentage = 1)

        salary_calculator = SalaryCalculator(accruals, deductions)

        Result = salary_calculator.calculate_net_salary() 
        self.assertEqual(round(Result, 1 ), 933140.0)

    """1st error unit test in the case of the number of extra daylight hours worked exceeds 60"""
    def testLimitOfExtraDaylightHours(self):
        accruals = Accruals(
            BasicSalary = 800000,
            WorkedDays = 30,
            HolidayTimeWorked = 0,
            ExtraDaylightHoursWorked = 80,
            ExtraNightHoursWorked = 0,
            HolidayExtraDaylightHoursWorked = 0,
            HolidayExtraNightHoursWorked = 0,
            DaysOfDisability = 0,
            LeaveDays = 5
    )
        with self.assertRaises(DataSizeLimitExceeded):
            VerifyLimitOfExtraDaylightHoursWorked(accruals.ExtraDaylighthoursworked)

    """2nd error unit test in the case of the number of extra night hours worked exceeds 60"""
    def testLimitOfExtraNightghtHours(self):
        accruals = Accruals(
            BasicSalary = 10000000,
            WorkedDays = 30,
            HolidayTimeWorked = 0,
            ExtraDaylightHoursWorked = 0,
            ExtraNightHoursWorked = 90,
            HolidayExtraDaylightHoursWorked = 0,
            HolidayExtraNightHoursWorked = 0,
            DaysOfDisability = 0,
            LeaveDays = 5
    )
        with self.assertRaises(DataSizeLimitExceeded):
            VerifyLimitOfExtraNightHoursWorked(accruals.ExtraNightHoursWorked)

    """3rd error unit test in the case of a negative salary parameter"""
    def testNegativeBasicSalary(self):
        accruals = Accruals(
            BasicSalary = -800000,
            WorkedDays = 30,
            HolidayTimeWorked = 0,
            ExtraDaylightHoursWorked = 0,
            ExtraNightHoursWorked = 0,
            HolidayExtraDaylightHoursWorked = 0,
            HolidayExtraNightHoursWorked = 0,
            DaysOfDisability = 0,
            LeaveDays = 5
    )
        with self.assertRaises(NegativeSalary):
            VerifyNegativeSalary(accruals.BasicSalary)

    """4th error unit test in the case of a negative worked days parameter"""
    def testNegativeWorkedDays(self):
        accruals = Accruals(
            BasicSalary = 800000,
            WorkedDays = -30,
            HolidayTimeWorked = 0,
            ExtraDaylightHoursWorked = 0,
            ExtraNightHoursWorked = 0,
            HolidayExtraDaylightHoursWorked = 0,
            HolidayExtraNightHoursWorked = 0,
            DaysOfDisability = 0,
            LeaveDays = 5
        )

        with self.assertRaises(IllegalParameters):
            VerifyNegativeWorkedDays(accruals.WorkedDays)

    """5th error unit test in the case of zero worked days"""
    def testZeroWorkedDays(self):
        accruals = Accruals(
            BasicSalary = 800000,
            WorkedDays = 0, 
            HolidayTimeWorked = 0,
            ExtraDaylightHoursWorked = 0,
            ExtraNightHoursWorked = 0,
            HolidayExtraDaylightHoursWorked = 0,
            HolidayExtraNightHoursWorked = 0,
            DaysOfDisability = 0,
            LeaveDays = 5
        )
        with self.assertRaises(IllegalParameters):
            VerifyNonZeroWorkedDays(accruals.WorkedDays)

    """6th error unit test in the case of a negative number of disability days"""
    def testNegativeDisabilityDays(self):
        accruals = Accruals(
            BasicSalary = 9500000,
            WorkedDays = 30, 
            HolidayTimeWorked = 1,
            ExtraDaylightHoursWorked = 3,
            ExtraNightHoursWorked = 0,
            HolidayExtraDaylightHoursWorked = 3,
            HolidayExtraNightHoursWorked = 0,
            DaysOfDisability = -4,
            LeaveDays = 5
        )
        with self.assertRaises(IllegalParameters):
            VerifyNegativeDisabilityDays(accruals.DaysOfDisability)

    """7th error unit test in the case of basic salary value is not numeric"""
    def testNumericBasicSalary(self):
        accruals = {
            "BasicSalary": "1000",
            "WorkedDays": 18, 
            "HolidayTimeWorked": 0,
            "ExtraDaylightHoursWorked": 3,
            "ExtraNightHoursWorked": 0,
            "HolidayExtraDaylightHoursWorked": 0,
            "HolidayExtraNightHoursWorked": 0,
            "DaysOfDisability": 0,
            "LeaveDays": 5
        }
        with self.assertRaises(DataTypeError):
            VerifyBasicSalaryDataTypeError(**accruals)

    """8th error unit test in the case of worked days value is not numeric"""
    def testNumericBasicSalary(self):
        accruals = {
            "BasicSalary": 1000000,
            "WorkedDays": "Hola", 
            "HolidayTimeWorked": 0,
            "ExtraDaylightHoursWorked": 3,
            "ExtraNightHoursWorked": 0,
            "HolidayExtraDaylightHoursWorked": 0,
            "HolidayExtraNightHoursWorked": 0,
            "DaysOfDisability": 0,
            "LeaveDays": 5
        }
        with self.assertRaises(DataTypeError):
            VerifyWorkedDaysDataTypeError(**accruals)

if __name__ == '_main_':
   unittest.main()