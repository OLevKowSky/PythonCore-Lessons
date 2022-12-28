from datetime import datetime, timedelta


users = [
    {"name": "Bill", "birthdate": "1990-12-24"},
    {"name": "Gill", "birthdate": "1990-12-25"},
    # {"name": "Till", "birthdate": "1990-12-26"},
    # {"name": "Dill", "birthdate": "1990-12-27"},
    {"name": "Bilg", "birthdate": "1990-12-24"},
    {"name": "Gilg", "birthdate": "1990-12-25"},
    # {"name": "Tilg", "birthdate": "1990-12-26"},
    # {"name": "Dilg", "birthdate": "1990-12-27"},
]

current_date = datetime(year=2022, month=12, day=19)

start_period = current_date - timedelta(days=current_date.weekday()) + timedelta(days=7)

end_period = start_period + timedelta(days=7)


def get_str_period(start_period: datetime, end_period: datetime) -> list[str]:
    delta = end_period - start_period  # as timedelta
    # days = [start_period + timedelta(days=i) for i in range(delta.days + 1)]
    # return {d.strftime("%m-%d"): d.strftime("%Y") for d in days}
    return delta

print(get_str_period(start_period, end_period))
    

# this_year_bd = {}

# period_bd = get_str_period(start_period, end_period)
# for user in users:
#     # user_bd = datetime.strptime(user["birthdate"], "%Y-%m-%d").date()
#     # cur_year_bd = user_bd.replace(year=current_date.year)
#     user_bd = user["birthdate"][5:]
#     if user_bd in list(period_bd):
#         print(user["name"])

#     if not this_year_bd.get(cur_year_bd):
#         this_year_bd[cur_year_bd] = [user["name"]]
#     else:
#         this_year_bd[cur_year_bd].append(user["name"])


# for k, v in this_year_bd.items():
#     print(f'{k.strftime("%A")}: {", ".join(v)}')