"""Lesson 9_2"""

## Decorators

# import time
#
#
# def slow_func(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(2)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @slow_func
# def countdown(number):
#     if number < 1:
#         print("Less then one")
#     else:
#         print(number)
#         countdown(number - 1)
#
#
# print(countdown(5))


# def repeat(num):
#     def decorator_repeat(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat
#
#
# @repeat(num=3)
# def greeting(name):
#     print(f"hello {name}")
#
#
# greeting("Denys")


# import random
#
# PLUGINS = dict()
#
# def register(func):
#     PLUGINS[func.__name__] = func
#     return func
#
#
# @register
# def greeting(name):
#     return f'Hello {name}'
#
#
# @register
# def good_bye(name):
#     return f"Good bye {name}"
#
#
# def random_greet_bye(name):
#     greeter, byer = random.choice(list(PLUGINS.items()))
#     print(f"Now {greeter}")
#     return byer(name)
#
# random_greet_bye("Alisa")
# print(list(PLUGINS.items()))


# import time
#
#
# def slow_func_1(func=None, *args, stop=1):
#     def dec_slow_func(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(stop)
#             return func(*args, **kwargs)
#         return wrapper
#     # return dec_slow_func
#
#     if func is None:
#         return dec_slow_func
#     else:
#         return dec_slow_func(func)
#
#
# @slow_func_1(stop=2)
# def countdown(number):
#     if number < 1:
#         print("Less then one")
#     else:
#         print(number)
#         countdown(number - 1)
#
#
# countdown(5)


## MAP

# x = list(map(lambda l: l.capitalize(), ["alisa", "bob", "mike"])) # швидше спрацює ніж нижчий код
# print(x)
#
# c = [l.capitalize() for l in ["alisa", "bob", "mike"]]
# print(c)

## FILTER

# even = lambda n: n % 2 == 0
# e = list(filter(even, range(20)))
# print(e)
#
# e_l = [e for e in range(20) if e % 2 == 0]
# print(e_l)


## Задачі

# s = [1.12345, 2.12345, 3.12345, 44.12345, 55.12345]
#
# res = list(map(round, s, range(1, 7)))
# print(res)


## ZIP

# empl = ["alisa", "bob", "mike", "ann"]
# salary = ["100", "200", "300", "400"]
# 
# res = list(zip(empl, salary)) # об"єднує в кортеж два списки
# print("ZIP", res)
#
# res = dict(zip(empl, salary)) # об"єднує в словник два списки
# print(res)

# empl_m = ["alisa", "bob", "mike", "ann"]
# salary_m = ["100", "200", "300", "400"]
#
# res_m = list(map(lambda e, s: (e,s), empl_m, salary_m))
# print("MAP", res_m)


# words = ("tenet", "civic", "madam", "kino", "car")
#
# pal = list(filter(lambda w: w == w[::-1], words))
# print(pal)


books = [
    {"Title": "Time", "Author": "Brown", "Price": 200},
    {"Title": "Kobzar", "Author": "Shevchenko", "Price": 300},
    {"Title": "Zapysky", "Author": "Kostenko", "Price": 500}
]

def book_func(books):
    if books["Price"] > 200:
        return True
    else:
        return False


filter_obj = filter(book_func, books)
for b in filter_obj:
    print(dict(b)["Title"])
