
from datetime import datetime, timedelta


def read_DB():

    with open("employees.txt") as file:
        
        employees = []
        lines = file.readlines()
        
        for employee in lines:
            employees.append(eval(employee)) 

        return employees


if __name__ == "__main__":
    read_DB()


employees = read_DB()
current_date = datetime.now().date()
start_period = current_date
end_period = start_period + timedelta(weeks=1)


def get_str_period(start_period, end_period):

    delta = end_period - start_period
    days = [start_period + timedelta(days=i) for i in range(delta.days + 1)]
    return days


if __name__ == "__main__":
    get_str_period(start_period, end_period)


def get_this_year_BD():

    this_year_BD = {}

    for employee in employees:
        employee_BD = datetime.strptime(employee["birthday"], "%Y/%m/%d").date()
        cur_year_BD = employee_BD.replace(year=current_date.year)

        if not this_year_BD.get(cur_year_BD):
            this_year_BD[cur_year_BD] = [employee["name"]]
        else:
            this_year_BD[cur_year_BD].append(employee["name"])

    return this_year_BD

if __name__ == "__main__":
    get_this_year_BD()


def get_birthdays_per_week():

    this_year_BD = get_this_year_BD()
    period_BD = get_str_period(start_period, end_period)

    for k, v in this_year_BD.items():
        if k in period_BD:
            if k.weekday() == 5:
                k = k + timedelta(days=2)
                print(f'{k.strftime("%A")}: {", ".join(v)}')
            elif k.weekday() == 6:
                k = k + timedelta(days=1)
                print(f'{k.strftime("%A")}: {", ".join(v)}')
            else:
                print(f'{k.strftime("%A")}: {", ".join(v)}')

if __name__ == "__main__":
    get_birthdays_per_week()
