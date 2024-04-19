"""unittest module is imported, which is the standard Python unit testing framework."""
import unittest

import sys
sys.path.append("src")

"""Payroll_Logic module is imported, which contains the program logic."""
import logic.Payroll_Logic as Payroll_Logic



"""A new class called PayrollTests is created, which inherits from unittest.TestCase."""
class PayrollTests(unittest.TestCase):

    """Unit test of the CalculateDailySalary method:
    1st normal unit test to verify that Calculate daily salary method works correctly"""
    def testCalculateDailySalary1(self):
        BasicSalary = 2000000
        WorkedDays = 30
        Result = Payroll_Logic.CalculateDailySalary(BasicSalary,WorkedDays )
        self.assertEqual(round(Result,1), 66666.7)

    """Unit test of the CalculatePayrollPayment01 method:
    2nd normal unit test to verify that Calculate payroll method works correctly"""
    def testCalculatePayrollPayment01(self):
        BasicSalary = 8000000
        TransportSubsidy = 0
        WorkedDays = 30
        HolidayTimeWorked = 1
        ExtraDaylightHoursWorked = 1
        ExtraNightHoursWorked = 0
        HolidayExtraDaylightHoursWorked = 0
        HolidayExtraNightHoursWorked = 0
        HealthInsurancePercentage = 4
        PensionContributionPercentage = 4
        PensionSolidarityFundContributionPercentage = 4
        DaysOfDisability = 0
        LeaveDays = 0
        Withholding = 733920
        Result = Payroll_Logic.CalculatePayrollPaymentCallingAllFunctions(BasicSalary, TransportSubsidy, WorkedDays, 
        HolidayTimeWorked, ExtraDaylightHoursWorked, ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked, 
        HolidayExtraNightHoursWorked, HealthInsurancePercentage, PensionContributionPercentage, 
        PensionSolidarityFundContributionPercentage, DaysOfDisability, LeaveDays, Withholding)
        self.assertEqual(round(Result, 1), 6512995)

    """Unit test of the HealthInsurance method:
    3rd normal unit test to verify that HealthInsurance method works correctly"""
    def testCalculateHealthInsurance(self):
        BasicSalary = 7500000
        HealthInsurancePercentage = 4
        Result = Payroll_Logic.CalculateHealthInsurance(BasicSalary, HealthInsurancePercentage)
        self.assertEqual(Result, 300000)

    """Unit test of the CalculatePensionContribution method:
    4th normal unit test to verify that CalculatePensionContribution method works correctly"""
    def testCalculatePensionContribution(self):
        BasicSalary = 7500000
        PensionContributionPercentage = 4
        Result = Payroll_Logic.CalculatePensionContribution(BasicSalary, PensionContributionPercentage)
        self.assertEqual(Result, 300000)

    """Unit test of the CalculatePensionSolidarityFundContribution method:
    5th normal unit test to verify that CalculatePensionSolidarityFundContribution method works correctly"""
    def testCalculatePensionSolidarityFundContribution(self):
        BasicSalary = 5000000
        PensionSolidarityFundContributionPercentage = 2
        Result = Payroll_Logic.CalculatePensionSolidarityFundContribution(BasicSalary, PensionSolidarityFundContributionPercentage)
        self.assertEqual(Result, 100000)

    """Unit test of the CalculateDisabilityTimeValue method:
    6th normal unit test to verify that CalculateDisabilityTimeValue method works correctly"""
    def testCalculateDisabilityTimeValue1(self):
        DailySalary = 70000
        DaysOfDisability = 2
        resultado = Payroll_Logic.CalculateDisabilityTimeValue(DailySalary, DaysOfDisability)
        self.assertEqual(round(resultado,1), 93324)

    """Unit test of the CalculateDisabilityTimeValue method:
    7th normal unit test to verify the calculation of disability value greater than 90 and less than 540 days."""
    def testCalculateDisabilityTimeValue2(self):
        DailySalary = 70000
        DaysOfDisability = 180
        Result = Payroll_Logic.CalculateDisabilityTimeValue(DailySalary, DaysOfDisability)
        self.assertEqual(round(Result,1), 6300000)


    """Unit test of the CalculatePayrollPayment method:
    1st exceptional unit test in the case that a person with a high salary also has high deductions"""
    def testCalculatePayrollPayment1(self):
        BasicSalary = 20000000
        TransportSubsidy = 0
        WorkedDays = 30
        HolidayTimeWorked = 0
        ExtraDaylightHoursWorked = 0
        ExtraNightHoursWorked = 0
        HolidayExtraDaylightHoursWorked = 0
        HolidayExtraNightHoursWorked = 0
        HealthInsurancePercentage = 7
        PensionContributionPercentage = 8
        PensionSolidarityFundContributionPercentage = 3
        DaysOfDisability = 0
        LeaveDays = 0
        Withholding = 290476.75
        Result = Payroll_Logic.CalculatePayrollPaymentCallingAllFunctions(BasicSalary, TransportSubsidy, WorkedDays, 
        HolidayTimeWorked, ExtraDaylightHoursWorked, ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked, 
        HolidayExtraNightHoursWorked, HealthInsurancePercentage, PensionContributionPercentage, 
        PensionSolidarityFundContributionPercentage, DaysOfDisability, LeaveDays, Withholding)
        self.assertEqual(round(Result, 1), 12143837)

    """Unit test of the CalculatePayrollPayment method:
    2nd exceptional unit test in the case of a high number of days of disability"""
    def testCalculatePayrollPayment2(self):
        BasicSalary = 1500000
        TransportSubsidy = 162000
        WorkedDays = 10
        HolidayTimeWorked = 0
        ExtraDaylightHoursWorked = 0
        ExtraNightHoursWorked = 0
        HolidayExtraDaylightHoursWorked = 0
        HolidayExtraNightHoursWorked = 0
        HealthInsurancePercentage = 4
        PensionContributionPercentage = 4
        PensionSolidarityFundContributionPercentage = 4
        DaysOfDisability = 20
        LeaveDays = 0
        Withholding = 0
        Result = Payroll_Logic.CalculatePayrollPaymentCallingAllFunctions(BasicSalary, TransportSubsidy, WorkedDays, HolidayTimeWorked, 
        ExtraDaylightHoursWorked, ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked, HolidayExtraNightHoursWorked, 
        HealthInsurancePercentage, PensionContributionPercentage, PensionSolidarityFundContributionPercentage, DaysOfDisability, LeaveDays,
        Withholding)
        self.assertEqual(round(Result,1), 1148600)

    """Unit test of the CalculatePayrollPayment method:
    3rd exceptional unit test in the case of a person who started working in the middle of the month"""
    def testCalculatePayrollPayment3(self):
        BasicSalary = 4000000
        TransportSubsidy = 0
        WorkedDays = 15
        HolidayTimeWorked = 0
        ExtraDaylightHoursWorked = 0
        ExtraNightHoursWorked = 0
        HolidayExtraDaylightHoursWorked = 0
        HolidayExtraNightHoursWorked = 0
        HealthInsurancePercentage = 4
        PensionContributionPercentage = 4
        PensionSolidarityFundContributionPercentage = 4
        DaysOfDisability = 0
        LeaveDays = 0
        Withholding = 0
        Result = Payroll_Logic.CalculatePayrollPaymentCallingAllFunctions(BasicSalary, TransportSubsidy, WorkedDays, HolidayTimeWorked, 
        ExtraDaylightHoursWorked, ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked, HolidayExtraNightHoursWorked, 
        HealthInsurancePercentage, PensionContributionPercentage, PensionSolidarityFundContributionPercentage, DaysOfDisability, LeaveDays,
        Withholding)
        self.assertEqual(round(Result, 1), 1520000)

    """Unit test of the TestCalculatePayrollPayment method:
    4th exceptional unit test in the case of a person worked a lot of extra hours"""
    def testCalculatePayrollPayment4(self):
        BasicSalary = 6000000
        TransportSubsidy = 0
        WorkedDays = 30
        HolidayTimeWorked = 0
        ExtraDaylightHoursWorked = 5
        ExtraNightHoursWorked = 6
        HolidayExtraDaylightHoursWorked = 5
        HolidayExtraNightHoursWorked = 5
        HealthInsurancePercentage = 4
        PensionContributionPercentage = 4
        PensionSolidarityFundContributionPercentage = 4
        DaysOfDisability = 0
        LeaveDays = 0
        Withholding = 290476.75
        Result = Payroll_Logic.CalculatePayrollPaymentCallingAllFunctions(BasicSalary, TransportSubsidy, WorkedDays, HolidayTimeWorked, 
        ExtraDaylightHoursWorked, ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked, HolidayExtraNightHoursWorked, 
        HealthInsurancePercentage, PensionContributionPercentage, PensionSolidarityFundContributionPercentage, DaysOfDisability, LeaveDays,
        Withholding)
        self.assertEqual(round(Result, 1), 5206654.2)

    """Unit test of the CalculatePayrollPayment method:
    5th exceptional unit test in the case of a high number of leave days"""
    def testCalculatePayrollPayment5(self):
        BasicSalary = 2500000
        TransportSubsidy = 162000
        WorkedDays = 5
        HolidayTimeWorked = 0
        ExtraDaylightHoursWorked = 0
        ExtraNightHoursWorked = 0
        HolidayExtraDaylightHoursWorked = 0
        HolidayExtraNightHoursWorked = 0
        HealthInsurancePercentage = 4
        PensionContributionPercentage = 4
        PensionSolidarityFundContributionPercentage = 4
        DaysOfDisability = 0
        LeaveDays = 25
        Withholding= 0
        Result = Payroll_Logic.CalculatePayrollPaymentCallingAllFunctions(BasicSalary, TransportSubsidy, WorkedDays, HolidayTimeWorked, 
        ExtraDaylightHoursWorked, ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked, HolidayExtraNightHoursWorked, 
        HealthInsurancePercentage, PensionContributionPercentage, PensionSolidarityFundContributionPercentage, DaysOfDisability, LeaveDays,
        Withholding)
        self.assertEqual(round(Result, 1), 2362000) 

    """Unit test of the CalculateValueOfHolidaysWorked method:
    6th exceptional unit test in the case of a high number of holidays worked"""
    def testCalculateValueOfHolidaysWorked(self):
        DailySalary = 70000
        HolidayTimeWorked = 5
        Result = Payroll_Logic.CalculateValueOfHolidaysWorked(DailySalary, HolidayTimeWorked)
        self.assertEqual(Result, 262500)

    """Unit test of the CalculatePayrollPayment method:
    7th exceptional unit test in the case of a person has minimum deductions"""
    def CalculatePayrollPayment6(self):
        BasicSalary = 800000
        TransportSubsidy = 0
        WorkedDays = 30
        HolidayTimeWorked = 0
        ExtraDaylightHoursWorked = 0
        ExtraNightHoursWorked = 0
        HolidayExtraDaylightHoursWorked = 0
        HolidayExtraNightHoursWorked = 0
        HealthInsurancePercentage = 2
        PensionContributionPercentage = 2
        PensionSolidarityFundContributionPercentage = 2
        DaysOfDisability = 0
        LeaveDays = 0
        Withholding = 733920.00
        Result = Payroll_Logic.CalculatePayrollPaymentCallingAllFunctions(BasicSalary, TransportSubsidy, WorkedDays, 
        HolidayTimeWorked, ExtraDaylightHoursWorked, ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked, 
        HolidayExtraNightHoursWorked, HealthInsurancePercentage, PensionContributionPercentage, 
        PensionSolidarityFundContributionPercentage, DaysOfDisability, LeaveDays, Withholding)
        self.assertEqual(round(Result, 1), 6786080)

    """Unit test of the VerifyTransportSubsidy method:
    1st error unit test in the case of a negative subsidy transport parameter"""
    def testVerifyTransportSubsidy(self):
        BasicSalary = 3000000
        TransportSubsidy = -5
        self.assertRaises(Payroll_Logic.IllegalParameters, Payroll_Logic.VerifyTransportSubsidy,TransportSubsidy)

    """Unit test of the CalculateLeaveDaysValue method:
    2nd error unit test in the case of a negative Leave Days parameter"""
    def CalculateLeaveDaysValue(self):
        DailySalary = 70000
        LeaveDays = -5
        self.assertRaises(Payroll_Logic.IllegalParameters, Payroll_Logic.CalculateLeaveDaysValue, DailySalary, LeaveDays)

    """Unit test of the VerifyNegativeSalary method:
    3rd error unit test in the case of a negative salary parameter"""
    def testVerifyNegativeSalary(self):
        BasicSalary = -1000000
        WorkedDays = 15
        self.assertRaises( Payroll_Logic.IllegalParameters,  Payroll_Logic.VerifyNegativeSalary, BasicSalary)

    """Unit test of the VerifyWorkedDaysParameter1 method:
    4th error unit test in the case of a negative worked days parameter"""
    def testVerifyWorkedDaysParameter1(self):
        BasicSalary = 3000000
        WorkedDays = -15
        self.assertRaises( Payroll_Logic.IllegalParameters,  Payroll_Logic.VerifyWorkedDaysParameter1, WorkedDays)

    """Unit test of the VerifyWorkedDaysParameter2 method:
    5th error unit test in the case of zero worked days parameter due to division by zero isn't defined"""
    def testVerifyWorkedDaysParameter2(self):
        BasicSalary = 3000000
        WorkedDays = 0
        self.assertRaises(Payroll_Logic.IllegalParameters, Payroll_Logic.VerifyWorkedDaysParameter2, WorkedDays)
    
    """Unit test of the VerifyBasicSalaryDifferentFromZero method:
    6th error unit test in the case of a basic salary is equal to zero"""
    def testVerifyBasicSalaryDifferentFromZero(self):
        BasicSalary = 0
        WorkedDays = 15
        self.assertRaises(Payroll_Logic.IllegalParameters, Payroll_Logic.VerifyBasicSalaryDifferentFromZero, BasicSalary, WorkedDays)
        
    """Unit test of the VerifyMaximumOfExtraHours method:
    7th error unit test in the case of a person worked more than 50 extra hours, which is not allowed."""
    def testVerifyMaximumOfExtraHours(self):

        ExtraDaylightHoursWorked = 0
        self.assertRaises(Payroll_Logic.IllegalParameters, Payroll_Logic.VerifyMaximumOfExtraHours, ExtraDaylightHoursWorked)
        
    """Unit test of the VerifyHealthInsurancePercentage method:
    8th error unit test in the case of a person whose salary is less than 4 SMLV has a health insurance of more than 4%."""
    def testVerifyHealthInsurancePercentage(self):
        BasicSalary = 2500000
        HealthInsurancePercentage = 8
        self.assertRaises(Payroll_Logic.IllegalParameters, Payroll_Logic.VerifyHealthInsurancePercentage, BasicSalary, HealthInsurancePercentage)

if __name__ == '_main_':
   unittest.main()