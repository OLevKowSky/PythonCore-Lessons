"""Lesson 9_0"""

# func = print
# func("acd")

# a = map(lambda x: x + 1, [1, 2, 3])
# print(a)

# def func(arg_func):
#     def inner():
#         return arg_func
#     return inner
#
# a = func
# a() # викликається функція "func"
# print(func)

# LEGB

# a = 3 # global scope
#
# def func(arg_func):
#     a = 2 # enclosed scope
#     def inner():
#         a = 1 # local scope
#         print(a)
#         return arg_func
#     return inner
#
#
# a = func
# a()
# print(func)

# enclosures

# def power(n): # аргумент, який ми хочемо конкретизувати, потрібно передавати у зовнішню функцію
#
#     # print(n) # 2
#
#     def enclosed(x):
#         return x ** n
#
#     return enclosed
#
#
# power_two = power(2)
# power_three = power(3)
# power_ten = power(10)
#
# print(power_two(3))
# print(power_three(2))
# print(power_ten(4))


# def power(n, y, z): # вкладенність може бути подвійною і більше
#
#     def enclosed(x, q, t):
#         return x ** n * y * z
#
#     return enclosed
#
#
# power_two = power(2, 3, 5)
#
# print(power_two(3, 3, 3))

# приклад з "game8_0.py"

# def move(direction):
#
#     def inner_move():
#
#         print(f"Moving {direction} from position ")
#
#         print(f"New position ")
#
#         return None
#
#     return inner_move
#
#
# move_up = move("up")
# move_down = move("down")
# move_left = move("left")
# move_right = move("right")
#
# move_up()
# move_down()
# move_left()
# move_right()

# Каррування

# def move_up(game_world, char_position):
#
#     log(f"Moving up from position {char_position}")
#
#     game_world[char_position[0]] [char_position[1]] = " "
#     char_position[0] -= 1
#     game_world[char_position[0]] [char_position[1]] = "X"
#
#     log(f"New position {char_position}")
#
#     return game_world, char_position
#   
#
# def move_down(game_world, char_position):
#
#     log(f"Moving down from position {char_position}")
#
#     game_world[char_position[0]] [char_position[1]] = " "
#     char_position[0] += 1
#     game_world[char_position[0]] [char_position[1]] = "X"
#
#     log(f"New position {char_position}")
#
#     return game_world, char_position
#
#
# def move_left(game_world, char_position):
#
#     log(f"Moving left from position {char_position}")
#
#     game_world[char_position[0]] [char_position[1]] = " "
#     char_position[1] -= 1
#     game_world[char_position[0]] [char_position[1]] = "X"
#
#     log(f"New position {char_position}")
#
#     return game_world, char_position
#
#
# def move_right(game_world, char_position):
#
#     log(f"Moving right from position {char_position}")
#
#     game_world[char_position[0]] [char_position[1]] = " "
#     char_position[1] += 1
#     game_world[char_position[0]] [char_position[1]] = "X"
#
#     log(f"New position {char_position}")
#
#     return game_world, char_position
#
#
# directions = {"up": move_up, "down": move_down, "left": move_left, "right": move_right}
#
# def move(direction): # обгортка карування
#     return directions[direction]


# SOLID - почитати


# Декоратори - додають функціонала об'єкту без його зміни.
# (Звичайно)Складається з двох функцій: внутрішньої та зовнішньої. Може їз трьох

# from time import time
#
#
# def check_performance(func):
#
#     def wrapper(*args, **kwargs): # якщо wrapper загального характеру зазначають (*args, **kwargs), тобто якщо не знаєш який аргумент(и) туди будете передавати(яку функцію огортати)
#
#         start = time()
#         func(*args, **kwargs)
#         print(time() - start)
#
#     return wrapper
#
#
# @check_performance     # "@" це декоратор, замісць # check_my_test_func = check_performance(my_test_func)
# def my_test_func(text):                            # check_my_test_func("asd")
#     print(text)
#
#
# # check_my_test_func = check_performance(my_test_func)
# # check_my_test_func("asd")
#
#
# my_test_func("asd")


# from time import time # приклад, коли в декоратор можна передавати аргумент "@check_performance(1)"
#
#
# def check_performance(a):
#
#     def inner_function(func):
#
#         def wrapper(*args, **kwargs):
#
#             print(a)
#     
#             start = time()
#             func(*args, **kwargs)
#             print(time() - start)
#
#         return wrapper
#
#     return inner_function
#
#
# @check_performance(1) 
# def my_test_func(text):
#     print(text)
#
#
# my_test_func("asd")


# from time import time # приклад, коли функція після декоратора повинна щось повернути
#
#
# def check_performance(a):
#
#     def inner_function(func):
#
#         def wrapper(*args, **kwargs):
#
#             print(a)
#          
#             start = time()
#             result = func(*args, **kwargs)
#             print(time() - start)
#
#             return result
#
#         return wrapper
#
#     return inner_function
#
#
# @check_performance(1) 
# def my_test_func(text):
#     return print(text)
#
#
# my_test_func("asd")

# Ітератор/Генератор

# for i in [1, 2, 3]:
#     print(i)
#
# my_list_iter = iter([1, 2, 3])
# print(next(my_list_iter))
# print(next(my_list_iter))
# print(next(my_list_iter))
#
#
# def for_(iterable_object): # теж саме, що попередні два коди
#
#     my_list_iter = iter(iterable_object)
#
#     while True:
#
#         try:
#             i = next(my_list_iter)
#         except StopIteration:
#             break
#
#         print(i)
#
#
# for_([1, 2, 3])


# def func():
#     print("value: 1")
#     yield 1
#     print("value: 2")
#     yield 2
#     print("value: 3")  
#     yield 3
#
# a = type(func())
# print(a)
#
# print(func())
#
# # print(next(func()))
# # print(next(func()))
# # print(next(func()))
#
# my_generator = func()
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
#
# for i in func():
#     print(i)


# b = 2
#
#
# def func():
#     print(b)
#     yield 1
#     print(b)
#     yield 2
#     print(b)  
#     yield 3
#
#
# my_generator = func()
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))


# def func(c):
#     c += 1
#     yield c
#     c += 1
#     yield c
#     c += 1
#     yield c
#
#
# my_generator = func(1)
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))


""""""


# import requests
#
#
# EXCHANGE_URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
# exchange_rate = requests.get(EXCHANGE_URL).json()
# print(exchange_rate)
#
# def exchange(ccy, base_ccy):
#     for i in exchange_rate:
#         if i["ccy"] == ccy.upper() and i["base_ccy"] == base_ccy.upper():
#             return i["buy"], i["sale"]
#
#
# EXCHANGES = {
#     "USD/UAH": lambda: exchange("usd", "uah"),
#     "EUR/UAH": lambda: exchange("eur", "uah"),
#     }
#
#
# def handle_exchange(ccy_ratio):
#     return EXCHANGES[ccy_ratio]
#
# print(handle_exchange("USD/UAH")())


# import requests
#
#
# EXCHANGE_URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
# exchange_rate = requests.get(EXCHANGE_URL).json()
# # print(exchange_rate)
#
# def exchange(ccy, base_ccy):
#     for i in exchange_rate:
#         if i["ccy"] == ccy.upper() and i["base_ccy"] == base_ccy.upper():
#             return i["buy"], i["sale"]
#
#
# EXCHANGES = {}
#
# EXCHANGES = {f"{i['ccy']}/{i['base_ccy']}": exchange for i in exchange_rate}
# print(EXCHANGES)
#
#
# def handle_exchange(ccy_ratio):
#     return EXCHANGES[ccy_ratio]
#
#
# print(handle_exchange("USD/UAH")("usd", "uah"))



