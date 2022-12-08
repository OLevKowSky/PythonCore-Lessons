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

from collections import ChainMap

first = {"fruit": "apple", "vegatable": "potato"}
second = {"color": "blue", "car": "volvo"}
third = {"name": "Alisa", "surname": "Simpson"}

new_map = ChainMap(first, second, third)
