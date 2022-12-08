"""Lesson 8_0. Addition matirial"""

# datetime

# from datetime import datetime
#
# def main():
#     user_input = input("Enter datetime in format dd.mm [-]: ")
#     user_entered_date = datetime.strptime(user_input, "%d.%m")
#     # print(user_entered_date)
#     current_date = datetime.now()
#     user_entered_date = user_entered_date.replace(year=current_date.year)
#     # print(user_entered_date)
#     if current_date > user_entered_date:
#         user_entered_date = user_entered_date.replace(year=current_date.year + 1)
#
#     target_date_str = datetime.strftime(user_entered_date, "%d %B")   
#     delta = user_entered_date - current_date   
#     print(f"{delta.days} days left till {target_date_str}")
#     print(f"{delta.seconds} seconds left till {target_date_str}")
#
#
# if __name__ == "__main__":
#     main()


# random generator

# import random
# from datetime import datetime, timedelta
#
#
# def main():
#     starting_date = input("Enter starting date: ")
#     end_date = input("Enter ending date: ")
#
#     starting_date = datetime.strptime(starting_date, "%Y-%m-%d")
#     end_date = datetime.strptime(end_date, "%Y-%m-%d")
#
#     interval_days = (end_date - starting_date).days
#     # print(interval_days)
#     days_delta = random.randint(0, interval_days + 1)
#     print(starting_date + timedelta(days=days_delta))
#
#
# if __name__ == "__main__":
#     main()

# choice, sample

# import random
#
# l = ["a", "b", "c"]
# print(random.choice(l))
# print(random.sample(l, k=2))

# decimal - контроль точності обчисленнь
#
# from decimal import *
#
# getcontext().prec=16
# print(Decimal(0.1) + Decimal(0.2))
#
# getcontext().prec=2
# print(Decimal(1)/Decimal(3) * 100)
# print(float(Decimal(1)/Decimal(3) * 100))

# math, cmath

# import math
# import cmath
#
# print(math.sin(math.pi))
# print(math.sin(math.pi / 2))
# print(math.exp(1))
# print(math.log10(100))
# print(math.log2(8))
# print(math.log(math.e))
#
# print(math.sqrt(4))
# # print(math.sqrt(-4)) # ValueError
# print(cmath.sqrt(-4))
#
# print(math.degrees(math.pi))
# print(math.degrees(math.pi/4))
# print(math.radians(180))
# print(math.radians(45))

# namedtuple

# import collections
#
# person1 = ("Bob", "Dou", 25)
#
# print(person1)
# print(person1[1])
#
# Person = collections.namedtuple("Person", ["name", "surname", "age"])
# person1 = Person("Bob", "Dou", 25)
#
# print(person1)
# print(person1[1])
# print(person1[-1])
# print(person1.name)
# print(person1.age)

# counter (collections)

# import collections
#
# s = "jnlbvabbcdas idnkadnsvv oianvlnasldnv dcjnbosoi"
# 
# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# 
# print(d)
#
# d = collections.Counter(s)
#
# print(d)
# print(d.most_common(2))

# defaultdict

# import collections
#
# l = ["apple", "banana", "apricot", "fd", "jbjdsb"]
# d = collections.defaultdict(list)
# for el in l:
#     d[el[0]].append(el)
#
# print(d)
#
# def a():
#     return 0
#
# d = collections.defaultdict(a)
# s = "jnlbvabbcdas idnkadnsvv oianvlnasldnv dcjnbosoi"
#
# for i in s:
#     d[i] += 1
#
# print(d)


# deque

# import collections
# 
# d = collections.deque(maxlen=5)
# for i in range(10):
#     d.append(i)
#
# print(d)

# def main():
#     user_inputs = []
#     while True:
#         user_input = input("[]: ")
#         user_inputs.append(user_input)
#         if len(user_inputs) > 5:
#             user_inputs = user_inputs[-5:]
#         if user_input == "q":
#             break
#     print(f"Last 5 inputs: {user_inputs}")
#
#
# if __name__ == "__main__":
#     main()

# import collections
#
# def main():
#     user_inputs = collections.deque(maxlen=5)
#     while True:
#         user_input = input("[]: ")
#         user_inputs.append(user_input)
#         if user_input == "q":
#             break
#     print(f"Last 5 inputs: {user_inputs}")
#
#
# if __name__ == "__main__":
#     main()

# comprehensions

# squers = []
#
# for i in range(11):
#     squers.append(i ** 2)
#
# print(squers)
#
# squares = [i ** 2 for i in range(11)]
# print(squers)

def func(x):
    return x * 2
#
# doubled = [func(i) for i in range(11)] # list
# print(doubled)
#
# doubled = {func(i) for i in range(11)} # set
# print(doubled)
#
doubled = {i: func(i) for i in range(11)} # dict
print(doubled)
