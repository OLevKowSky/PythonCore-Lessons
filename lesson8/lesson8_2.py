"""Lesson 8_2"""

# defaultdict

# from collections import defaultdict
# import random

# new = defaultdict(str)
#
# new[1] = "White"
# new[2] = "Black"
# new[3] = "Blue"
#
# for n in range(1, 10):
#     print(new[n])

# new = defaultdict(str)
# list_of_colors = ["Red", "Yellow", "Orange", "Green"]
#
# new[1] = "White"
# new[2] = "Black"
# new[3] = "Blue"
#
# for key in range(0, 7):
#     if new[key] == "":
#         new[key] = list_of_colors[random.randint(0, 3)]
#
# print(new)

# namedtuple

# from collections import namedtuple
#
# person = namedtuple("person", "name, job, age")
#
# person1 = person("Alisa", "developer", "25")
#
# print("Detail of person1: ", person1)
# print("Preson's 1 job ", person1.job)
# print(type(person1))

# counter

#from collections import Counter
#
# c = Counter("The yellow yellow list")
# 
# print(c)
#
# animals = Counter(("dog", "turtele", "panda"))
# animals["dog"] = 0
#
# print(animals)
#
# del animals["dog"]
#
# print(animals)

# from collections import ChainMap
#
# first = {"fruit": "apple", "vegatable": "potato"}
# second = {"color": "blue", "car": "volvo"}
# third = {"name": "Alisa", "surname": "Simpson"}
#
# new_map = ChainMap(first, second, third)
# # print(new_map)
#
# fourth = {"job": "developer"}
#
# new_map.new_child(fourth) # не спрацював
# print("New ChainMap ", new_map)

# datetime, IANA

# dateutil

# from dateutil import tz
# from datetime import datetime
#
# now = datetime.now(tz=tz.tzlocal())
# print(now)
# print("Name of time zone ", now.tzname())
#
# London_tz = tz.gettz("Europe/London")
# now1 = datetime.now(tz=London_tz)
# print(now1)
# print("Name1 of time zone ", now1.tzname())

# from dateutil import parser, tz
# from datetime import datetime
#
# new_date = parser.parse("December 08, 2022 2:50 PM")
# new_date = new_date.replace(tzinfo=tz.gettz("America/New_York"))
# now = datetime.now(tz=tz.tzlocal())
#
# result = new_date - now
#
# print(f"Time US: {result}")

# для HW8 1:20

# from calendar import monthrange
#
# m = monthrange(2022, 12)
# print(m)

# from datetime import date
#
# a = (date(2022, 12, 1) - date(2022, 11, 1)).days
# print(a)

# timedelta

# from datetime import datetime, timedelta
#
# now = datetime.now()
# print(now)
#
# tomorrow = timedelta(days=+1)
#
# # print(now + tomorrow)
#
# delta = timedelta(days=+4, hours=-4)
#
# print(now + delta)

# relativedelta

# from datetime import datetime
# from dateutil.relativedelta import relativedelta
#
# now = datetime.now()
# print(now)
#
# delta = relativedelta(years=+3, month=+1, days=+4, hours=+2, minutes=-25)
# print("Relative delta ", now + delta)

# iso format

from datetime import date
from datetime import datetime

date.fromisoformat("2022-12-08")
a = datetime.date
print(a)

date_string = "12-07-2022 21:02:00"
format_string = "%m-%d-%Y %H:%M:%S"

a = datetime.strptime(date_string, format_string)
print(a)

# import dateparser
#
# a = dateparser.parse("yesterday")
# b = dateparser.parse("morgen")
# print(a)
# print(b)
