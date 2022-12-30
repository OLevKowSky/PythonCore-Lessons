"""lesson 9_1 Closure, Decorators, Lambda, Iter/Gen"""

## Closure

# age = 25
#
# def birthday():
#     age = 30
#     print("Function age", age)
#
#
# birthday()
# print("Global age ", age)


# def countdown(start):
#     # Enclosing function
#     def display():
#         # Nested function
#         n = start
#         while n > 0:
#             n -= 1
#             print("countdown ", n)
#
#     display()
#
#
# countdown(5)


# from urllib.request import urlopen
#
# def page(url):
#     def get():
#         return urlopen(url).read()
#     return get
#
# url_apple = page("https://www.apple.com")
# # print(url_apple)
# u = url_apple.__closure__[0].cell_contents
# print(u)


## Decorators

# def my_decorator(func):
#     def wrapper():
#         print("First print")
#         func()
#         print("Second print")
#     return wrapper()
#
# def say_hello():
#     print("Hello")
#
# say_hello = my_decorator(say_hello)
# print(say_hello)


# def my_decorator(func): # теж саме, що і попередня функція, тільки з декоратором "@"
#     def wrapper():
#         print("First print")
#         func()
#         print("Second print")
#     return wrapper()
#
# @my_decorator
# def say_hello():
#     print("Hello")


# from decorators import new_dec
#
# @new_dec
# def say_hello(name):
#     print("Hello ", name)
#
# say_hello("Alisa")
#
# from decorators import timer
#
# @timer
# def func_some_time(num):
#     for _ in range(num):
#         sum([i**2 for i in range(5000)])
#
#
# func_some_time(1000)


## LAMBDA

# def hello(name):
#     return name
#
# lambda name: name


# def l(x):
#     return x + 1
#
# l = lambda x: x + 1
# print(l(3))
# 
# l1 = (lambda x: x + 1)(3)
# print(l1)


# full_name = lambda first_name, last_name: f"Full name: {first_name.title()} {last_name.title()}"
#
# print(full_name("alisa", "simpson"))

# l1 = (lambda x, y: x + y)(2, 2)
# print(l1)

# ll1 = lambda x, y: x + y
# print(type(ll1))


# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f"Trace-back.func: {func.__name__}, args:{args}, kwargs:{kwargs}")
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @trace
# def add_nam(x):
#     return x + 4
#
# print(add_nam(5))
#
# print((trace(lambda x: x ** 2))(5))


## Iterators

# iter_obj = iter([3, 4, 5]) # 3
# print(iter_obj)
# print(next(iter_obj))

# iter_obj = iter([3, 4, 5]) # 3, 4
# print(iter_obj)
# print(next(iter_obj))
# print(next(iter_obj))

# iter_obj = iter([3, 4, 5]) # 3, 4, 5
# print(iter_obj)
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# iter_obj = iter([3, 4, 5]) # 3, 4, 5, StopIteration
# print(iter_obj)
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# iter_tuple = iter(("alisa", "bob", "mike")) # "alisa", "bob", "mike"
# print(next(iter_tuple))
# print(next(iter_tuple))
# print(next(iter_tuple))

# iter_obj = iter(("alisa"))
# print(type(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))


## Generators

def even(x):
    while (x!=0):
        if x % 2 == 0:
            yield x
        x -= 1
       
for i in even(10):
    print(i)

print(even(10).__sizeof__())
print(iter([10, 8, 6, 4, 2]).__sizeof__())
