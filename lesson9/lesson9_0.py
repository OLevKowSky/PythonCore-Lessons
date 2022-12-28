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


# def power(n, y, z): # вкліденність може бути подвійною і більше
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


from time import time # приклад, коли функція після декоратора повинна щось повернути


def check_performance(a):

    def inner_function(func):

        def wrapper(*args, **kwargs):

            print(a)
            
            start = time()
            result = func(*args, **kwargs)
            print(time() - start)

            return result

        return wrapper

    return inner_function


@check_performance(1) 
def my_test_func(text):
    return print(text)


my_test_func("asd")
