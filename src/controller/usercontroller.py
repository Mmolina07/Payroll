import psycopg2
import sys
sys.path.append("src")
import controller.SecretConfig as SecretConfig
from model.Payroll_Logic import *


class ErrorNotfound( Exception ):
    """Exception indicating that a searched row was not found"""
    pass

def GetCursor( ) :
    connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER,
                                password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
    return connection.cursor()

def CreateTable():
    connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER,
                                password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
    cursor = connection.cursor()
    cursor.execute("""create table employees (
        firstname text not null,
        surname text not null,
        idnumber varchar( 20 ) PRIMARY KEY NOT NULL,
        mail text
        );""")
    connection.commit()


def DeleteTable():

    sql = "drop table employees;"
    cursor = GetCursor()
    cursor.execute( sql )
    cursor.connection.commit()

def Deletelines():

    """Danger!"""
    sql = "delete from employees;"
    cursor = GetCursor()
    cursor.execute( sql )
    cursor.connection.commit()


def DeleteById(employee):
    sql = f"delete from employees where idnumber = '{employee.idnumber}'"
    cursor = GetCursor()
    cursor.execute( sql )
    cursor.connection.commit()


def Insert( employee : Employee):
    """ Guarda un Usuario en la base de datos """
    try:
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = GetCursor()
        cursor.execute(f"""insert into employees (
            firstname,   surname,  idnumber,  mail
        )
        values 
        (
            '{employee.firstname}',  '{employee.surname}', '{employee.idnumber}', '{employee.mail}'
        );
                        """)
        
    
        cursor.connection.commit()
    except :
        cursor.connection.rollback()
        raise Exception ("Id repeated. It was not possible to add the employee: " + employee.idnumber)
    
def Update( employee: Employee ):
    """
    Actualiza los datos de un usuario en la base de datos

    El atributo cedula nunca se debe cambiar, porque es la clave primaria
    """
    cursor = GetCursor()
    cursor.execute(f"""
        update employees
        set 
            firstname='{employee.firstname}',
            surname='{employee.surname}',
            mail='{employee.mail}'
        where idnumber='{employee.idnumber}'
    """)
    # Las instrucciones DDL y DML no retornan resultados, por eso no necesitan fetchall()
    # pero si necesitan commit() para hacer los cambios persistentes
    cursor.connection.commit()
        

def SearchById(idnumber):

    cursor = GetCursor()
    consulta = f"""SELECT firstname, surname, idnumber, mail
                from employees where idnumber = '{idnumber}' """
    cursor = GetCursor()
    cursor.execute(consulta)

    result = cursor.fetchone()

    if result is not None:
        # If a result is found, create an Employee object
        return Employee(result[0], result[1], result[2], result[3])
    else:
        # If no result is found, return message
        raise ErrorNotfound("Employee not found")
    

def CreateAccrualsTable():
    connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER,
                                password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
    cursor = connection.cursor()
    cursor.execute("""create table accruals (
                    BasicSalary varchar( 20 ) not null,
                    WorkedDays varchar( 20 ) not null,
                    HolidayTimeWorked varchar( 20 ) PRIMARY KEY NOT NULL,
                    ExtraDaylightHoursWorked varchar( 20 ) not null,
                    ExtraNightHoursWorked varchar( 20 ) not null,
                    HolidayExtraDaylightHoursWorked varchar( 20 ) not null,
                    HolidayExtraNightHoursWorked varchar( 20 ) not null,
                    DaysOfDisability varchar( 20 ) not null,
                    LeaveDays varchar( 20 ) not null                     
        );""")
    connection.commit()


def InsertAccruals(accruals: Accruals):
    """ Guarda un Usuario en la base de datos """
    cursor = GetCursor()
    cursor.execute(f"""insert into accruals (
        BasicSalary, WorkedDays, HolidayTimeWorked, ExtraDaylightHoursWorked, ExtraNightHoursWorked,
        HolidayExtraDaylightHoursWorked, HolidayExtraNightHoursWorked, DaysOfDisability, LeaveDays               
    )
    values 
    (
        '{accruals.BasicSalary}',  '{accruals.WorkedDays}', '{accruals.holidaytimeworked}', '{accruals.ExtraDaylighthoursworked}',
        '{accruals.ExtraNightHoursWorked}',  '{accruals.HolidayExtraDaylightHoursworked}',
        '{accruals.HolidayExtraNightHoursWorked}', '{accruals.DaysOfDisability}', '{accruals.LeaveDays}'
    );
                    """)
    

    cursor.connection.commit()
    

def CreateTableDeductions():
    
    connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER,
                                password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
    cursor = connection.cursor()
    cursor.execute("""create table Deductions (
        HealthInsurancePercentage varchar( 5 ) NOT NULL,
        PensionContributionPercentage varchar( 5 ) NOT NULL,
        PensionSolidarityFundContributionPercentage varchar( 5 ) NOT NULL
        );""")
    connection.commit()


def InsertDeductions( deductions:Deductions):
    """ Guarda un Usuario en la base de datos """
    cursor = GetCursor()
    cursor.execute(f"""insert into deductions (HealthInsurancePercentage, PensionContributionPercentage, PensionSolidarityFundContributionPercentage          
    )
    values 
    (
        '{deductions.HealthInsurancePercentage}',  '{deductions.PensionContributionPercentage}',
        '{deductions.PensionSolidarityFundContributionPercentage}'
    );
    """)
    cursor.connection.commit()


# Función que busca por nombre

def SearchByNameAndSurname(firstname, surname):

    cursor = GetCursor()
    consulta = f"""SELECT firstname, surname, idnumber, mail
                from employees where firstname = '{firstname}' and surname = '{surname}' """
    cursor = GetCursor()
    cursor.execute(consulta)

    result = cursor.fetchone()

    if result is not None:
        return Employee(result[0], result[1], result[2], result[3])
    else:
        return None
    