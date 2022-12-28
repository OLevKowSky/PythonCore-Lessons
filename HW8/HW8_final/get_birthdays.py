from datetime import datetime, timedelta
from HW8 import *


def task():
    
    employees = read_DB()
    current_date = datetime.now().date()
    start_period = current_date
    end_period = start_period + timedelta(weeks=1)

    get_str_period(start_period, end_period)
    get_this_year_BD()
    get_birthdays_per_week()


if __name__ == "__main__":
    task()
