
from datetime import datetime

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
    week_begin = datetime(year=2022, month=12, day=28)
    week_end = datetime(year=2022, month=12, day=30)
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
    employees = this_year_BD()

    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    saturday = []
    sunday = []


    for bday in suit_bday_lst:

        bday = bday.strftime("%Y/%m/%d")
        
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





# from datetime import datetime, timedelta

# def read_DB(): # читає базу данних з текстового файлу

#     with open("employees.txt") as file:
        
#         employees = []
#         lines = file.readlines()
        
#         for employee in lines:
#             employees.append(eval(employee)) 

#         return employees # повертає список словників з днями народження


# read_DB()


# employees = read_DB()
# current_date = datetime.now().date()
# start_period = current_date
# end_period = start_period + timedelta(weeks=1)


# def get_str_period(start_period: datetime, end_period: datetime) -> list[str]:
#     delta = end_period - start_period  # as timedelta
#     days = [start_period + timedelta(days=i) for i in range(delta.days + 1)]
#     return days # [d.strftime("%Y/%m/%d") for d in days]

# get_str_period(start_period, end_period)


# this_year_BD = {}

# period_BD = get_str_period(start_period, end_period)

# for employee in employees:
#     employee_BD = datetime.strptime(employee["birthday"], "%Y/%m/%d").date()
#     cur_year_BD = employee_BD.replace(year=current_date.year)

#     if not this_year_BD.get(cur_year_BD):
#         this_year_BD[cur_year_BD] = [employee["name"]]
#     else:
#         this_year_BD[cur_year_BD].append(employee["name"])

# for k, v in this_year_BD.items():
#     if k in period_BD:
#         if k.weekday() == 5:
#             k = k + timedelta(days=2)
#             print(f'{k.strftime("%A")}: {", ".join(v)}')
#         elif k.weekday() == 6:
#             k = k + timedelta(days=1)
#             print(f'{k.strftime("%A")}: {", ".join(v)}')
#         else:
#             print(f'{k.strftime("%A")}: {", ".join(v)}')