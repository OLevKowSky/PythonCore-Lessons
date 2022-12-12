"""Lesson 9_0"""

# func = print
# func("acd")

# map(lambda x: x = 1, [1, 2, 3])

# def func(arg_func):
#     def inner():
#         return arg_func
#     return inner

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


# def power(n, y, z):
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

def move_up(game_world, char_position):

    log(f"Moving up from position {char_position}")

    game_world[char_position[0]] [char_position[1]] = " "
    char_position[0] -= 1
    game_world[char_position[0]] [char_position[1]] = "X"

    log(f"New position {char_position}")

    return game_world, char_position
    

def move_down(game_world, char_position):

    log(f"Moving down from position {char_position}")

    game_world[char_position[0]] [char_position[1]] = " "
    char_position[0] += 1
    game_world[char_position[0]] [char_position[1]] = "X"

    log(f"New position {char_position}")

    return game_world, char_position


def move_left(game_world, char_position):

    log(f"Moving left from position {char_position}")

    game_world[char_position[0]] [char_position[1]] = " "
    char_position[1] -= 1
    game_world[char_position[0]] [char_position[1]] = "X"

    log(f"New position {char_position}")

    return game_world, char_position


def move_right(game_world, char_position):

    log(f"Moving right from position {char_position}")

    game_world[char_position[0]] [char_position[1]] = " "
    char_position[1] += 1
    game_world[char_position[0]] [char_position[1]] = "X"

    log(f"New position {char_position}")

    return game_world, char_position


move = {"up" : move_up, "down" : move_down, "left" : move_left, "right": move_right}


# SOLID - почитати