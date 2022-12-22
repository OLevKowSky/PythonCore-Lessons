
from datetime import datetime

def read_DB():

    with open("employees.txt") as file:

        # employees = file.readlines()
        # employees = [employee.rstrip('\n') for employee in employees]
        
        employees = []
        lines = file.readlines()
        
        for employee in lines:
            employees.append(eval(employee)) 

        return employees


read_DB()


def this_year_bday():

    employees = read_DB()
    current_year = datetime.now()
    this_bday_lst = []

    for employee in employees:
        bday = datetime.strptime(employee["birthday"], "%Y/%m/%d")
        this_bday = bday.replace(year=current_year.year)
        this_bday_lst.append(this_bday)

    return print(this_bday_lst)


this_year_bday()


def this_year_BD():

    employees = read_DB()
    current_year = datetime.now()

    for employee in employees:
        bday = datetime.strptime(employee["birthday"], "%Y/%m/%d")
        this_bday = bday.replace(year=current_year.year)
        this_bday_str = this_bday.strftime("%Y/%m/%d")
        employee["birthday"] = this_bday_str

    return print(employees)


this_year_BD()


            # if bday in employee["birthday"]:
            #     if bday_of_empl.weekday() == 0:
            #         print("Monday", employee["name"])
            #     elif bday_of_empl.weekday() == 1:
            #         print("Tuesday", employee["name"])
            #     elif bday_of_empl.weekday() == 2:
            #         print("Wednesday", employee["name"])
            #     elif bday_of_empl.weekday() == 3:
            #         print("Thursday", employee["name"])
            #     elif bday_of_empl.weekday() == 4:
            #         print("Friday", employee["name"])
            #     elif bday_of_empl.weekday() == 5:
            #         print("Saturday", employee["name"])
            #     elif bday_of_empl.weekday() == 6:
            #         print("Sunday", employee["name"])

            # if bday in employee["birthday"]:
            #     print(bday_of_empl.weekday(), employee["name"])