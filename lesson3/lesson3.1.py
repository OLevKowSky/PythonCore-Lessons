"""FUNCTIONS"""

# def greeting():
#     print("Hello")
#
#
# greeting()

# def greeting(name):
#     print(f"Hello {name}")
#
#
# greeting("Alisa")

# def greeting(first_name, last_name):
#     print(f"Hello {first_name} {last_name}")
#
#
# greeting("Alisa", "Simpson")

# def greeting(last_name, first_name):
#     print(f"Hello {first_name} {last_name}")
#
#
# greeting(first_name="Alisa", last_name="Simpson")

# def greeting(last_name, first_name):
#     return f"Hello {first_name} {last_name}"
#
#
# print(greeting(first_name="Alisa", last_name="Simpson"))

# def person(first_name, last_name, age, profile="developer"):
#     return f"Hello {first_name} {last_name}, you have {age} year old, you are {profile}"
#
#
# print(person("Alisa", "Simpson", 22))

# def person(first_name, last_name, age, profile="developer"):
#     return f"Hello {first_name} {last_name}, you have {age} year old, you are {profile}"
#
#
# print(person("Alisa", "Simpson", 22, "QA"))

# def person(first_name, last_name, age, profile="developer"):
#     last_name = ""    # = None
#     return f"Hello {first_name} {last_name}, you have {age} year old, you are {profile}"
#
#
# print(person("Alisa", "Simpson", 22, "QA"))

# def person(first_name: str, last_name: str, age: int, profile="developer") -> str:
#     """This function about person
#     first_name: person name, type string
#     :returne string
#     """
#     return f"Hello {first_name} {last_name}, you have {age} year old, you are {profile}"
#
#
# print(person("Alisa", "Simpson", 22, "QA"))

# def calc(x, y):
#     x = 2
#     y = 3
#     return x + y
#
#
# print(calc(2, 2))

# import math # example dont run, just for understanding LEGB
#
# t = 5
# c = 7
#
# def calc(func):
#     y = "B"
#     def greet():
#         x = "A"
#         print("Hello", x, y, t, math.sqrt(10))

# name = "Bob"
#
# def greeting():
#     global name
#     print(f"Hello global {name}")
#
#     name = "Alisa"
#     print(f"Hello {name}")
#
#
# greeting()
# print("Name ", name)

# ARGS & KWARGS

# def some_func(*args):
#     for arg in args:
#         print(arg)
#
#
# some_func("Hello", "Alisa", "you", "are", "developer", 4, 5)
#
# def dict_func(**kwargs):
#     for key, value in kwargs.items():
#         print("Key: ", key, "Value: ", value)
#
#
# dict_func(first_name = "alisa", second_name = "simpsom", age = 20)

# def super_function(param1, param2, *args, **kwargs):
#     print(f"param1 = {param1}")
#     print(f"param2 = {param2}")
#     print(f"args = {args}")
#     print(f"kwargs = {kwargs}")
#
#
# super_function(3, 5, "alisa", "developer", age=20, salary=1000, location="New-York")

# def function_one():
#     s = "hello"
#
#     def function_two():
#         print(s)
#
#
#     function_two()
#
#
# function_one()

# Recursion

# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(12))

# def countdown(n):
#     print(f"Countdown {n}")
#     if n == 0:
#        return
#     else:
#         countdown(n - 1)
#
#
# print(countdown(10))


def countdown(n):
    print(f"Countdown {n}")
    if n == 0:
        return
    else:
        countdown(n - 1)


countdown(10)

if __name__ == "__main__":
    countdown(5)
