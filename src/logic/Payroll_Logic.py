"""The following functions calculate the accruals, which are all the items for which an employee receives remuneration."""

"""Personalized exception management"""
class IllegalParameters(Exception):
    pass

"""This function calculates the employee's daily salary"""
def CalculateDailySalary(BasicSalary, WorkedDays):

    """If the user entered a total of 30 days worked"""
    Monthly = 30 

    """If the user entered a total of 15 days worked"""
    Fortnight = 15 

    if WorkedDays == Monthly:
        DailySalary = BasicSalary / WorkedDays
    else:
        WorkedDays == Fortnight
        DailySalary =  (BasicSalary / 2) / Fortnight

    return DailySalary

def CalculateTotalSalary(DailySalary, WorkedDays):
    
    TotalSalary = DailySalary * WorkedDays

    return TotalSalary

"""This function evaluates an error case where the basic salary cannot be zero if worked days are different from zero."""
def VerifyBasicSalaryDifferentFromZero(BasicSalary, WorkedDays):

    if BasicSalary == 0 and WorkedDays != 0:
        raise IllegalParameters( "The basic salary cannot be zero if the days worked are different from zero." )

"""This function evaluates an error case where the parameter entered as basic salary is negative."""
def VerifyNegativeSalary(BasicSalary):
    
    if BasicSalary < 0:
        raise IllegalParameters( "The basic salary cannot be negative." )
    
"""This function evaluates an error case where the parameter entered as WorkedDays is negative."""
def VerifyWorkedDaysParameter1(WorkedDays):
     
     if WorkedDays < 0:
        raise IllegalParameters("The time worked cannot be a negative number.")

"""This function evaluates an error case where the parameter entered as WorkedDays is zero."""
def VerifyWorkedDaysParameter2(WorkedDays):
    if WorkedDays == 0 :
        raise IllegalParameters("Division by zero cannot be calculated.")

"""This function evaluates an error case where the parameter entered as TransportSubsidy is negative."""
def VerifyTransportSubsidy(TransportSubsidy):
    if TransportSubsidy < 0:
        raise IllegalParameters("The transportation subsidy cannot be negative.")
    
"""This function calculates the transportation subsidy"""
def CalculateTransportSubsidy(BasicSalary, TransportSubsidy):

    """The minimum salary in Colombia is 1300000COP, so two minimum salaries are 2600000COP."""
    TwoCurrentLegalMinimumSalaries = 2600000

    """By law the employee is entitled to the transportation subsidy if the salary is less than or equal to 2600000COP"""
    if BasicSalary > TwoCurrentLegalMinimumSalaries and TransportSubsidy != 0:
        TransportSubsidy = 0

        print("You do not apply for the transportation subsidy because your salary must be less than or equal to 2600000COP.")
    else:
        TransportSubsidy = TransportSubsidy

    return TransportSubsidy

"""This function calculates the surcharge value of a worked holiday according to the legal surcharge."""
def CalculateValueOfHolidaysWorked(DailySalary, HolidayTimeWorked):

    """The surcharge for holiday hours worked according to the law is 75%."""
    HolidaySurchargePercentage = 0.75

    HolidayRecharge = (DailySalary * HolidaySurchargePercentage) * HolidayTimeWorked
    return HolidayRecharge

"""This function calculates the surcharge value of daylight extra hours worked, using the value established by law."""
def CalculateDaylightExtraHoursCharge(ExtraDaylightHoursWorked):

    """The value for a daylight hour worked according to the law is 6915COP."""
    DaylightHourSurcharge = 6915

    DaylightSurchageValue = DaylightHourSurcharge * ExtraDaylightHoursWorked
    return DaylightSurchageValue

"""This function calculates the surcharge value of night extra hours worked, using the value established by law."""
def CalculateExtraNigthHoursCharge(ExtraNightHoursWorked):

    """The surcharge for night hours worked according to the law is 9681COP."""
    NightHourSurchage = 9681

    NigthSurchargeValue = NightHourSurchage * ExtraNightHoursWorked
    return NigthSurchargeValue

"""This function evaluates an error case when extra hours exceeds 50 hours per month."""
def VerifyMaximumOfExtraHours(HolidayExtraNightHoursWorked):
    
    """Only 50 hours of overtime that can be worked per month will be paid according to the law."""
    MaximumOfExtraHours = 50
    if HolidayExtraNightHoursWorked <= MaximumOfExtraHours:
        raise IllegalParameters("No more than 50 hours of overtime per month may be paid.")

"""This function calculates the value of daylight extra hours on worked holidays using the value established by law."""
def CalculateHolidayExtraDaylightHoursWorkedValue(HolidayExtraDaylightHoursWorked):

    """The surcharge for a holiday extra daylight hour worked according to the law is 11064COP."""
    HolidayExtraDaylightHoursWorkedSurcharge = 11064
    HolidayExtraDaylightHoursWorkedSurchargeValue = HolidayExtraDaylightHoursWorkedSurcharge * HolidayExtraDaylightHoursWorked
    
    return HolidayExtraDaylightHoursWorkedSurchargeValue

"""This function calculates the value of night extra hours on worked holidays using the value established by law."""
def CalculateHolidayExtraNightHoursWorkedValue(HolidayExtraNightHoursWorked):

    """The surcharge for a holiday extra night hour worked according to the law is 13830COP."""
    HolidayExtraNightHoursWorkedSurcharge = 13830
    HolidayExtraNightHoursWorkedSurchargeValue = HolidayExtraNightHoursWorkedSurcharge * HolidayExtraNightHoursWorked
    
    return HolidayExtraNightHoursWorkedSurchargeValue

"""The following functions calculate the deductions which are the discounts that are made at the time of paying the salary to the employees."""

"""This function calculates the employee's health contribution according to the base salary and the health insurance percentage entered"""
def CalculateHealthInsurance(BasicSalary, HealthInsurancePercentage):
    HealthInsuranceValue = BasicSalary * (HealthInsurancePercentage/100)

    return HealthInsuranceValue

"""This function evaluates an error case where an employee earning less than 5848000 contributes more than 4% to health."""
def VerifyHealthInsurancePercentage(BasicSalary, HealthInsurancePercentage):
    """People earning less than 4 legal minimum salaries cannot contribute more than 4% to health"""
    MaximumSalaryToContribute4 = 5848000
    if BasicSalary < MaximumSalaryToContribute4 and HealthInsurancePercentage > 4:
        raise IllegalParameters("The health contribution cannot exceed 4 percentage for people earning less than 5848000")


"""This function calculates the pension contribution based on the basic salary and the percentage entered."""
def CalculatePensionContribution(BasicSalary, PensionContributionPercentage):
    PensionContributionValue = BasicSalary * (PensionContributionPercentage/100)

    return PensionContributionValue

"""This function calculates the contribution to the pension solidarity fund based on the basic salary and the percentage entered."""
def CalculatePensionSolidarityFundContribution(BasicSalary, PensionSolidarityFundContributionPercentage):
    PensionSolidarityFundContributionValue = BasicSalary * (PensionSolidarityFundContributionPercentage/100)

    return PensionSolidarityFundContributionValue

"""This function calculates the value to be paid according to the days of disability entered based on the daily salary."""
def CalculateDisabilityTimeValue(DailySalary, DaysOfDisability):
    
    """The law establishes that a surcharge of 0.6666 must be made to the daily
    salary per day of disability if these are in the range of 1 to 90 days."""
    
    """-The law establishes that a surcharge of 0.5 must be made to the daily
    salary per day of disability if these are in the range of 90 to 540 days."""
    
    """-The law establishes that there is no surcharge for disability if it exceeds
    540 days, since the health entity is the one who must pay."""

    if DaysOfDisability >= 1 and DaysOfDisability <= 90: 
        DaysOfDisabilityValue = 0.6666 * DailySalary
        TotalDisabilityValue = DaysOfDisabilityValue * DaysOfDisability

    elif DaysOfDisability > 90 and DaysOfDisability <= 540:
        DaysOfDisabilityValue = 0.5 * DailySalary
        TotalDisabilityValue = DaysOfDisabilityValue * DaysOfDisability

    else:
        TotalDisabilityValue = 0

    return TotalDisabilityValue    
    
"""Function that calculates the value to be paid according to the days of leave entered based 
on the basic salary, according to the law, these days are paid as a normal day."""

def CalculateLeaveDaysValue1(DailySalary, LeaveDays):
    
    LeaveDaysValue = DailySalary * LeaveDays
    return LeaveDaysValue
"""This function evaluates an error case where the leave days parameter is negative."""

def CalculateLeaveDaysValue(LeaveDays):
    if LeaveDays < 0:
        raise IllegalParameters( "Number of leave days cannot be negative" )
    

def CalculateWithholdingTax(BasicSalary):
    
    """The value of the current taxable value unit is 47065 according to the law."""
    ActualTaxableValueUnit = 47065   

    """We calculate the taxable base in Actual Taxable value unit"""
    """This function converts the basic salary to the Tax base"""

    TaxBase = BasicSalary / ActualTaxableValueUnit

    """The ranges for calculating the withholding tax are:
    from 0 to 95 with a marginal rate of 0%;
    from 95 to 150 with a marginal rate of 19%;
    from 150 to 360 with a marginal rate of 28%;
    from 360 to 640 with a marginal rate of 33%;
    from 640 to 945 with a marginal rate of 35%;
    from 945 to 2300 with a marginal rate of 37%;
    from 2300 and upwards with a marginal rate of 39%"""

    RangeTaxableValueUnit1 = 95  
    RangeTaxableValueUnit2 = 150
    RangeTaxableValueUnit3 = 360
    RangeTaxableValueUnit4 = 640
    RangeTaxableValueUnit5 = 945
    RangeTaxableValueUnit6 = 2300

    """Depending on the basic salary converted to uvt, the function determines the range in which the salary falls, applies the formula
    with its corresponding marginal rate and Taxable value unit aggregate."""

    """Withholding percentage comes from the range and the marginal rate"""

    """The constant is a Taxable value added to the formula for calculating the withholding tax"""


    if TaxBase > RangeTaxableValueUnit1 and TaxBase < RangeTaxableValueUnit2:

        WithholdingPercentage = 0.19
        WithholdingTax = (TaxBase - RangeTaxableValueUnit1) * WithholdingPercentage

    elif TaxBase > RangeTaxableValueUnit2 and TaxBase < RangeTaxableValueUnit3:

        WithholdingPercentage = 0.28
        WithholdingTax = (TaxBase - RangeTaxableValueUnit2) * WithholdingPercentage + 10
    
    elif TaxBase > RangeTaxableValueUnit3 and TaxBase < RangeTaxableValueUnit4:

        WithholdingPercentage = 0.33
        WithholdingTax = (TaxBase - RangeTaxableValueUnit3) * WithholdingPercentage + 69
    
    elif TaxBase > RangeTaxableValueUnit4 and TaxBase < RangeTaxableValueUnit5:

        WithholdingPercentage = 0.35
        WithholdingTax = (TaxBase - RangeTaxableValueUnit4) * WithholdingPercentage + 162
    
    elif TaxBase > RangeTaxableValueUnit5 and TaxBase < RangeTaxableValueUnit6:

        WithholdingPercentage = 0.37
        WithholdingTax = (TaxBase - RangeTaxableValueUnit5) * WithholdingPercentage + 268
    
    elif TaxBase > RangeTaxableValueUnit6:

        WithholdingPercentage = 0.39
        WithholdingTax = (TaxBase - RangeTaxableValueUnit6) * WithholdingPercentage + 770
    
    else:
        """There is not withholding whenever the salary is under the limit"""
        WithholdingTax = 0

    """We convert the withholding to pesos"""

    WithholdingCOP = WithholdingTax * ActualTaxableValueUnit

    return WithholdingCOP

"""This function calculates the total of accruals by adding the calculated value of each one above"""
def CalculateAccruals(TotalSalary, TransportSubsidy, HolidayRecharge, DaylightSurchageValue, NigthSurchargeValue, 
                      HolidayExtraDaylightHoursWorkedSurchargeValue, HolidayExtraNightHoursWorkedSurchargeValue,
                      TotalDisabilityValue, LeaveDaysValue):
    
    TotalAccruals = (TotalSalary + TransportSubsidy + HolidayRecharge + DaylightSurchageValue + NigthSurchargeValue + 
                HolidayExtraDaylightHoursWorkedSurchargeValue + HolidayExtraNightHoursWorkedSurchargeValue + TotalDisabilityValue 
                + LeaveDaysValue)
    
    return TotalAccruals

"""This function calculates the total of deductions by adding the calculated value of each one above"""
def CalculateDeductions(HealthInsuranceValue, PensionContributionValue, PensionSolidarityFundContributionValue,WitholdingCOP):

    TotalDeductions = (HealthInsuranceValue + PensionContributionValue + PensionSolidarityFundContributionValue + WitholdingCOP)
    
    return TotalDeductions

"""This function calculates the total payment by subtracting the total deductions from the total accruals."""
def CalculatePayment(TotalAccruals, TotalDeductions):
    Payment = TotalAccruals - TotalDeductions
    return Payment

"""This function calls all the previous functions and returns the total value to be paid."""
def CalculatePayrollPaymentCallingAllFunctions(BasicSalary, TransportSubsidy, WorkedDays, HolidayTimeWorked, ExtraDaylightHoursWorked, 
                            ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked, HolidayExtraNightHoursWorked, 
                            HealthInsurancePercentage, PensionContributionPercentage, PensionSolidarityFundContributionPercentage, 
                            TotalDisabilityValue, LeaveDays, Withholding):
    
    """All functions are individually called with their parameters"""
    DailySalary= CalculateDailySalary(BasicSalary, WorkedDays)
    TotalSalary = CalculateTotalSalary(DailySalary, WorkedDays) 
    TransportSubsidy = CalculateTransportSubsidy(BasicSalary, TransportSubsidy)
    HolidayRecharge = CalculateValueOfHolidaysWorked(DailySalary, HolidayTimeWorked)
    DaylightSurchageValue = CalculateDaylightExtraHoursCharge(ExtraDaylightHoursWorked)
    NigthSurchargeValue = CalculateExtraNigthHoursCharge(ExtraNightHoursWorked)

    HolidayExtraDaylightHoursWorkedSurchargeValue = CalculateHolidayExtraDaylightHoursWorkedValue(HolidayExtraDaylightHoursWorked)
    HolidayExtraNightHoursWorkedSurchargeValue = CalculateHolidayExtraNightHoursWorkedValue(HolidayExtraNightHoursWorked)
    
    HealthInsuranceValue = CalculateHealthInsurance(BasicSalary, HealthInsurancePercentage)
    PensionContributionValue = CalculatePensionContribution(BasicSalary, PensionContributionPercentage)
    PensionSolidarityFundContributionValue = CalculatePensionSolidarityFundContribution(BasicSalary, PensionSolidarityFundContributionPercentage)
    TotalDisabilityValue = CalculateDisabilityTimeValue(DailySalary, TotalDisabilityValue)
    LeaveDaysValue = CalculateLeaveDaysValue1(DailySalary, LeaveDays)
    Withholding = CalculateWithholdingTax(BasicSalary)

    TotalAccruals = CalculateAccruals(TotalSalary, TransportSubsidy, HolidayRecharge, DaylightSurchageValue, NigthSurchargeValue, 
                                      HolidayExtraDaylightHoursWorkedSurchargeValue, HolidayExtraNightHoursWorkedSurchargeValue, 
                                      TotalDisabilityValue, LeaveDaysValue)
    
    TotalDeductions = CalculateDeductions(HealthInsuranceValue, PensionContributionValue, PensionSolidarityFundContributionValue, Withholding)

    TotalPayment = CalculatePayment(TotalAccruals, TotalDeductions)

    print("The salary is: ", TotalSalary)
    print("The transportation allowance is: ", TransportSubsidy)
    print("The value to be paid for holidays is: ", HolidayRecharge)
    print("The value to be paid for daylight extra hours is: ", DaylightSurchageValue)
    print("The value to be paid for night extra hours is: ", NigthSurchargeValue)
    print("The value to be paid for holiday extra daylight hours is: ", HolidayExtraDaylightHoursWorkedSurchargeValue)
    print("The value to be paid for holiday night extra hours is: ", HolidayExtraNightHoursWorkedSurchargeValue)
    print("The value of the health contribution is: ", HealthInsuranceValue)
    print("The value of the pension contribution is:", PensionContributionValue)
    print("The value of the solidarity fund contribution is:  ", PensionSolidarityFundContributionValue)
    print("The value of the disability days is: ", TotalDisabilityValue)
    print("The value of leave days is: ", LeaveDaysValue)
    print(f"The value of the withholding tax for ${BasicSalary:.2f}: is ${Withholding:.2f}")
    print(f"The total value to be paid is: {TotalPayment:.1f}" )
    return TotalPayment