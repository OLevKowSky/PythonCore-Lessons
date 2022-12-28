from datetime import datetime, timedelta

def get_str_period(start_period: datetime, end_period: datetime) -> dict[str, str]:
    delta = end_period - start_period # as timedelta
    days = [start_period + timedelta(days=i) for i in range(delta.days + 1)]
    return {d.strftime("%m/%d"): d.strftime("%Y") for d in days}


print(get_str_period(datetime(2022, 12, 26), datetime(2023, 1, 2)).keys())