
from datetime import datetime, timedelta

def read_DB(): # читає базу данних з текстового файлу

    with open("employees.txt") as file:

        # employees = file.readlines()
        # employees = [employee.rstrip('\n') for employee in employees]
        
        employees = []
        lines = file.readlines()
        
        for employee in lines:
            employees.append(eval(employee)) 

        return employees # повертає список словників з днями народження


read_DB()


# employees = read_DB()

# for employee in employees:
#     print(employee.get("birthday"))

def this_year_bday(): # створює дати с днями народження в поточному році

    employees = read_DB()
    current_year = datetime.now()
    this_bday_lst = []

    for employee in employees:
        bday = datetime.strptime(employee["birthday"], "%Y/%m/%d")
        this_bday = bday.replace(year=current_year.year)
        this_bday_lst.append(this_bday)

    return this_bday_lst # повертає список днів народження в поточному році


this_year_bday()


def this_year_BD(): # перезаписує дні народження поточного року в нову базу данних

    employees = read_DB()
    current_year = datetime.now()

    for employee in employees:
        bday = datetime.strptime(employee["birthday"], "%Y/%m/%d")
        this_bday = bday.replace(year=current_year.year)
        this_bday_str = this_bday.strftime("%Y/%m/%d")
        employee["birthday"] = this_bday_str

    return employees # повертає список словників з днями народження поточного року


this_year_BD()


def compare(): # чи попадає дата народження в діапазон
    this_bday_lst = this_year_bday()
    week_begin = datetime.now() + timedelta(weeks=1)
    week_end = datetime.now() + timedelta(weeks=2)
    suit_bday_lst = []
    # print(type(week_begin))

    for this_bday in this_bday_lst:
        # print(type(this_bday))

        if week_begin <= this_bday <= week_end:
            # print(this_bday)
            suit_bday_lst.append(this_bday)
    
    suit_bday_lst = set(suit_bday_lst)

    return suit_bday_lst # повертає список днів народження в діапазоні


compare()


def name():

    suit_bday_lst = compare()
    # print(type(suit_bday_lst))
    employees = this_year_BD()
    # print(type(employees))
    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    saturday = []
    sunday = []


    for bday in suit_bday_lst:

        bday = bday.strftime("%Y/%m/%d")
        # print(type(bday))
        
        for employee in employees:

            bday_of_empl = datetime.strptime(employee["birthday"], "%Y/%m/%d")

            if bday in employee["birthday"]:
                
                if bday_of_empl.weekday() == 0:
                    monday.append(employee["name"])
                elif bday_of_empl.weekday() == 1:
                    tuesday.append(employee["name"])
                elif bday_of_empl.weekday() == 2:
                    wednesday.append(employee["name"])
                elif bday_of_empl.weekday() == 3:
                    thursday.append(employee["name"])
                elif bday_of_empl.weekday() == 4:
                    friday.append(employee["name"])
                elif bday_of_empl.weekday() == 5:
                    saturday.append(employee["name"])
                elif bday_of_empl.weekday() == 6:
                    sunday.append(employee["name"])

    if len(monday) != 0:
        print(f"Monday: {monday}")
    if len(tuesday) != 0:
        print(f"Tuesday: {tuesday}")
    if len(wednesday) != 0:
        print(f"Wednesday: {wednesday}")
    if len(thursday) != 0:
        print(f"Thursday: {thursday}")
    if len(friday) != 0:
        print(f"Friday: {friday}")
    if len(saturday) != 0:
        print(f"Saturday: {saturday}")
    if len(sunday) != 0:
        print(f"Sunday: {sunday}")


name()
