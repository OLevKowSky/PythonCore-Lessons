from datetime import datetime, timedelta

employees = [
    {"name" : "Maksym Bogush", "birthday" : "1978/01/09"},
    {"name" : "Olena Marchenko", "birthday" : "1983/01/09"},
    {"name" : "Dmytro Yashchenko", "birthday" : "1991/01/10"},
    {"name" : "Roman Demchenko", "birthday" : "1984/01/10"},
    {"name" : "Anna Metiolkina", "birthday" : "1986/01/11"},
    {"name" : "Vasyl Kizlenko", "birthday" : "1987/01/11"},
    # {"name" : "Oleksii Koptilyi", "birthday" : "1989/01/12"},
    # {"name" : "Kateryna Chernykh", "birthday" : "1980/01/12"},
    # {"name" : "Alina Omelchenko", "birthday" : "1993/01/13"},
    # {"name" : "Yuliia Vasylyshyna", "birthday" : "1995/01/13"},
    # {"name" : "Svitlana Kolisnyk", "birthday" : "1990/01/14"},
    # {"name" : "Oleksii Vysokos", "birthday" : "1995/01/14"},
    # {"name" : "Nataliia Ishchenko", "birthday" : "1991/01/15"},
    # {"name" : "Yuliia Aleksandrova", "birthday" : "1985/01/15"},
    # {"name" : "Iryna Luferova", "birthday" : "1982/01/16"},
    # {"name" : "Vadym Trykisha", "birthday" : "1989/01/16"}
]


current_date = datetime(year=2023, month=1, day=2).date()

start_period = current_date - timedelta(days=current_date.weekday()) + timedelta(days=7)

# def get_str_period(start_period: datetime, end_period: datetime) -> dict[str, str]:
#     delta = end_period - start_period # as timedelta
#     days = [start_period + timedelta(days=i) for i in range(delta.days + 1)]
#     return {d.strftime("%m/%d"): d.strftime("%Y") for d in days}


# print(get_str_period(datetime(2022, 12, 26), datetime(2023, 1, 2)).keys())

# print(start_period)

this_year_bd = {}

for employee in employees:
    bd = datetime.strptime(employee["birthday"], "%Y/%m/%d").date()

    cur_year_bd = bd.replace(year=current_date.year)

    if not this_year_bd.get(cur_year_bd):
        this_year_bd[cur_year_bd] = [employee["name"]]
    else:
        this_year_bd[cur_year_bd].append(employee["name"])


for k, v in this_year_bd.items():
    print(f"{k.strftime('%A')}: {', '.join(v)}")
