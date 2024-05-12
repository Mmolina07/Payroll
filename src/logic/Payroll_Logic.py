"""The following functions calculate the accruals, which are all the items for which an employee receives remuneration."""

"""Personalized exception management"""
class IllegalParameters(Exception):
    pass

class Employee:

    def __init__(self, Name, Id, accruals):
        self.Name = Name
        self.Id = Id
        self.accruals = accruals


class Accruals:
    
    def __init__(self, BasicSalary, WorkedDays, HolidayTimeWorked, ExtraDaylightHoursWorked,
                ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked,
                HolidayExtraNightHoursWorked, DaysOfDisability, LeaveDays):
        
        self.BasicSalary = BasicSalary
        self.WorkedDays = WorkedDays
        self.holidaytimeworked = HolidayTimeWorked
        self.ExtraDaylighthoursworked = ExtraDaylightHoursWorked
        self.ExtraNightHoursWorked = ExtraNightHoursWorked
        self.HolidayExtraDaylightHoursworked = HolidayExtraDaylightHoursWorked
        self.HolidayExtraNightHoursWorked = HolidayExtraNightHoursWorked
        self.DaysOfDisability = DaysOfDisability
        self.LeaveDays = LeaveDays 

    def CalculateDailySalary(self):

        Monthly = 30

        if self.WorkedDays == Monthly:
            DailySalary = self.BasicSalary / self.WorkedDays
        
        else:
            DailySalary = (self.BasicSalary / Monthly)

        return DailySalary
    
    def CalculateTotalSalary(self):
        DailySalary = self.CalculateDailySalary()

        TwoCurrentLegalMinimumSalaries = 2600000

        TransportSubsidyValue = 162000
        
        TotalSalary = DailySalary * self.WorkedDays

        if self.BasicSalary <= TwoCurrentLegalMinimumSalaries:
            TotalSalary += TransportSubsidyValue
        
        else:
            TotalSalary = TotalSalary

        return TotalSalary
    
    def CalculateValueOfHolidaysWorked(self, DailySalary):
        """The surcharge for holiday hours worked according to the law is 75%."""
        HolidaySurchargePercentage = 0.75

        HolidayRecharge = (DailySalary * HolidaySurchargePercentage) * self.holidaytimeworked
        return HolidayRecharge

    def CalculateDaylightExtraHoursCharge(self):
        """The value for a daylight hour worked according to the law is 6915COP."""
        DaylightHourSurcharge = 6915

        DaylightSurchargeValue = DaylightHourSurcharge * self.ExtraDaylighthoursworked
        return DaylightSurchargeValue

    def CalculateExtraNigthHoursCharge(self):
        """The surcharge for night hours worked according to the law is 9681COP."""
        NightHourSurcharge = 9681

        NightSurchargeValue = NightHourSurcharge * self.ExtraNightHoursWorked
        return NightSurchargeValue
    
    """This function calculates the value of daylight extra hours on worked holidays using the value established by law."""
    def CalculateHolidayExtraDaylightHoursWorkedValue(self):

        """The surcharge for a holiday extra daylight hour worked according to the law is 11064COP."""
        HolidayExtraDaylightHoursWorkedSurcharge = 11064
        HolidayExtraDaylightHoursWorkedSurchargeValue = HolidayExtraDaylightHoursWorkedSurcharge * self.HolidayExtraDaylightHoursworked
        
        return HolidayExtraDaylightHoursWorkedSurchargeValue

    """This function calculates the value of night extra hours on worked holidays using the value established by law."""
    def CalculateHolidayExtraNightHoursWorkedValue(self):

        """The surcharge for a holiday extra night hour worked according to the law is 13830COP."""
        HolidayExtraNightHoursWorkedSurcharge = 13830
        HolidayExtraNightHoursWorkedSurchargeValue = HolidayExtraNightHoursWorkedSurcharge * self.HolidayExtraNightHoursWorked
        
        return HolidayExtraNightHoursWorkedSurchargeValue
    
    def CalculateDisabilityTimeValue(self):
        if self.DaysOfDisability >= 1 and self.DaysOfDisability <= 90: 
            DaysOfDisabilityValue = 0.6666 * self.CalculateDailySalary()
            TotalDisabilityValue = DaysOfDisabilityValue * self.DaysOfDisability
            print("check1", TotalDisabilityValue)

        elif self.DaysOfDisability > 90 and self.DaysOfDisability <= 540:
            DaysOfDisabilityValue = 0.5 * self.CalculateDailySalary()
            TotalDisabilityValue = DaysOfDisabilityValue * self.DaysOfDisability

        else:
            TotalDisabilityValue = 0

        return TotalDisabilityValue
    
    def CalculateLeaveDaysValue(self):
        DailySalary = self.CalculateDailySalary()
        LeaveDaysValue = DailySalary * self.LeaveDays
        return LeaveDaysValue
    
    def calculate_total_accruals(self):
        total_accruals = 0
        total_accruals += self.CalculateTotalSalary()
        total_accruals += self.CalculateValueOfHolidaysWorked(self.CalculateDailySalary())
        total_accruals += self.CalculateDaylightExtraHoursCharge()
        total_accruals += self.CalculateExtraNigthHoursCharge()
        total_accruals += self.CalculateHolidayExtraDaylightHoursWorkedValue()
        total_accruals += self.CalculateHolidayExtraNightHoursWorkedValue()
        total_accruals += self.CalculateDisabilityTimeValue()
        total_accruals += self.CalculateLeaveDaysValue()

        return total_accruals

 
class Deductions:

    def __init__(self, accruals, HealthInsurancePercentage, PensionContributionPercentage,
                PensionSolidarityFundContributionPercentage):
        
        self.accruals = accruals
        self.HealthInsurancePercentage = HealthInsurancePercentage
        self.PensionContributionPercentage = PensionContributionPercentage
        self.PensionSolidarityFundContributionPercentage = PensionSolidarityFundContributionPercentage

    def CalculateHealthInsurance(self):
        total_accruals = self.accruals.calculate_total_accruals()
        HealthInsuranceValue = total_accruals * (self.HealthInsurancePercentage/100)
        return HealthInsuranceValue

    def CalculatePensionContribution(self):
        total_accruals = self.accruals.calculate_total_accruals()
        PensionContributionValue = total_accruals* (self.PensionContributionPercentage/100)
        return PensionContributionValue
    
    def CalculatePensionSolidarityFundContribution(self):
        total_accruals = self.accruals.calculate_total_accruals()
        PensionSolidarityFundContributionValue = total_accruals * (self.PensionSolidarityFundContributionPercentage/100)
        return PensionSolidarityFundContributionValue
    
        
    def CalculateWithholdingTax(self):
        """The value of the current taxable value unit is 47065 according to the law."""
        ActualTaxableValueUnit = 47065   

        """We calculate the taxable base in Actual Taxable value unit"""
        """This function converts the basic salary to the Tax base"""
        TaxBase = self.accruals.BasicSalary / ActualTaxableValueUnit

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
            TaxValueUnitinRange = 10
            WithholdingTax = (TaxBase - RangeTaxableValueUnit2) * WithholdingPercentage + TaxValueUnitinRange
        
        elif TaxBase > RangeTaxableValueUnit3 and TaxBase < RangeTaxableValueUnit4:
            WithholdingPercentage = 0.33
            TaxValueUnitinRange = 69
            WithholdingTax = (TaxBase - RangeTaxableValueUnit3) * WithholdingPercentage + TaxValueUnitinRange
        
        elif TaxBase > RangeTaxableValueUnit4 and TaxBase < RangeTaxableValueUnit5:
            WithholdingPercentage = 0.35
            TaxValueUnitinRange = 162
            WithholdingTax = (TaxBase - RangeTaxableValueUnit4) * WithholdingPercentage + TaxValueUnitinRange
        
        elif TaxBase > RangeTaxableValueUnit5 and TaxBase < RangeTaxableValueUnit6:
            WithholdingPercentage = 0.37
            TaxValueUnitinRange = 268
            WithholdingTax = (TaxBase - RangeTaxableValueUnit5) * WithholdingPercentage + TaxValueUnitinRange
        
        elif TaxBase > RangeTaxableValueUnit6:
            WithholdingPercentage = 0.39
            TaxValueUnitinRange = 770
            WithholdingTax = (TaxBase - RangeTaxableValueUnit6) * WithholdingPercentage + TaxValueUnitinRange
        
        else:
            """There is not withholding whenever the salary is under the limit"""
            WithholdingTax = 0

        """We convert the withholding to pesos"""
        WithholdingCOP = WithholdingTax * ActualTaxableValueUnit

        return WithholdingCOP
    
    def calculate_total_deductions(self):
        total_deductions = 0
        total_deductions += self.CalculateHealthInsurance()
        total_deductions += self.CalculatePensionContribution()
        total_deductions += self.CalculatePensionSolidarityFundContribution()
        total_deductions += self.CalculateWithholdingTax()
        return total_deductions


class SalaryCalculator:

    def __init__(self, accruals, deductions):
        self.accruals = accruals
        self.deductions = deductions

    def calculate_net_salary(self):
        total_accruals = self.accruals.calculate_total_accruals()
        total_deductions = self.deductions.calculate_total_deductions()

        net_salary = total_accruals - total_deductions

        return net_salary


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
        

    """This function evaluates an error case when extra hours exceeds 50 hours per month."""
    def VerifyMaximumOfExtraHours(HolidayExtraNightHoursWorked):
        
        """Only 50 hours of overtime that can be worked per month will be paid according to the law."""
        MaximumOfExtraHours = 50
        if HolidayExtraNightHoursWorked <= MaximumOfExtraHours:
            raise IllegalParameters("No more than 50 hours of overtime per month may be paid.")


    """This function evaluates an error case where an employee earning less than 5848000 contributes more than 4% to health."""
    def VerifyHealthInsurancePercentage(BasicSalary, HealthInsurancePercentage):
        """People earning less than 4 legal minimum salaries cannot contribute more than 4% to health"""
        MaximumSalaryToContribute4 = 5848000
        if BasicSalary < MaximumSalaryToContribute4 and HealthInsurancePercentage > 4:
            raise IllegalParameters("The health contribution cannot exceed 4 percentage for people earning less than 5848000")


accruals = Accruals(BasicSalary=1500000, WorkedDays=10, HolidayTimeWorked=0, ExtraDaylightHoursWorked=0,
                    ExtraNightHoursWorked=0, HolidayExtraDaylightHoursWorked=0,
                    HolidayExtraNightHoursWorked=0,  
                    DaysOfDisability=20, LeaveDays=0)

# Crear una instancia de la clase Deductions
deductions = Deductions(accruals, HealthInsurancePercentage=4, PensionContributionPercentage=4, 
                        PensionSolidarityFundContributionPercentage=4)


# Crear una instancia de la clase SalaryCalculator
calculator = SalaryCalculator(accruals, deductions)

# Imprimir los resultados
print("Salario diario:", accruals.CalculateDailySalary())
print("Salario total:", accruals.CalculateTotalSalary())
print("Valor de días festivos trabajados:", accruals.CalculateValueOfHolidaysWorked(accruals.CalculateDailySalary()))
print("Valor de horas extra diurnas:", accruals.CalculateDaylightExtraHoursCharge())
print("Valor de horas extra nocturnas:", accruals.CalculateExtraNigthHoursCharge())
print("Valor de horas extra diurnas en días festivos:", accruals.CalculateHolidayExtraDaylightHoursWorkedValue())
print("Valor de horas extra nocturnas en días festivos:", accruals.CalculateHolidayExtraNightHoursWorkedValue())
print("Valor del tiempo de incapacidad:", accruals.CalculateDisabilityTimeValue())
print("Valor de los días de licencia:", accruals.CalculateLeaveDaysValue())

print("retencion", deductions.CalculateWithholdingTax())
print("Seguro de salud:", deductions.CalculateHealthInsurance())
print("Contribución a la pensión:", deductions.CalculatePensionContribution())
print("Contribución al Fondo de Solidaridad Pensional:", deductions.CalculatePensionSolidarityFundContribution())


print("Salario neto:", calculator.calculate_net_salary())
