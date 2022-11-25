"""Lesson 4. Preparation"""

# my_list = ['a', 'b', 'c', 'd', 'e', 'f']
# for i in (my_list):
#     print(i)

# for i in range(len(my_list)):
#     print(i)

# for i in range(len(my_list)):
#     print(my_list[i])

# for index, element in enumerate(my_list):
#     print(index, element)

# for i in reversed(my_list):
#     print(i)

# for i in sorted(my_list):
#     print(i)

# def func(*my_list):
#
#     print(my_list)
#
#     return my_list
#
#
# func([1, 2, 3, 4])

# a = [1, 2, 3, 4]
# func(a)

# world_map = [[' ', ' ', ' '],
#              [' ', ' ', ' '],
#              [' ', ' ', ' ']]
#
# world_map[0][0] = 'X'
#
# for row in world_map:
#     print(row)

"""4.1. інший лектор"""

# [expression for element in iterable if condition] # синтаксис

# nums =[]
# for x in range(21):
#     if x % 2 == 0:
#         nums.append(x)
#
# print(nums)

# nums = [x for x in range(21) if x % 2 == 0]
# print(nums)

# nums = [x**2 for x in range(21)]
# print(nums)

# names = ['Bob', 'Bill', 'Jack']
# names2 = [s for s in names if 'a' in s]
# print(names2)

# nums = [x for x in range(21) if x % 2 == 0 if x % 5 == 0]
# print(nums)

# a = ['Yes' if x % 2 == 0 else 'No' for x in range(10)]
# print(a)

# l = [1, 2, 3, 4, 5]
#
# bb =['Yes' if v == 1 else 'No' if v == 2 else 'some another value' for v in l]
# print(bb)

# dict = {<new_key>:<new_value> for element in <iterable>} # загальний синтаксис для генератора словників

# import random

# customers = ["Bob", "Jack", "Lisa"]
# dict_new = {customer:random.randint(1, 100) for customer in customers}
# print(dict_new)

# nums = [1, 2, 3, 4, 5, 6, 7]
#
# e = {n: n**2 for n in nums if n % 2 == 0}
# print(e)

# nums = [1, 2, 3, 4, 5, 6, 7]
# new_set = {item**2 for item in nums}
# print(new_set)

# a = "nkncdncjlsbc t5 djfhrbd63nf38d"
#
# b = [int(num) for num in a if num.isdigit()]
# print(b)

# v = [item for item in range(0, 200) if item % 30 == 0 or item % 35 == 0]
# print(v)

# v = [abs(item) for item in range(-100, 200) if item % 30 == 0 or item % 35 == 0]
# print(v)

# from pathlib import Path  # для папки "test0" в терміналі вводимо "python .\lesson4.0.py test0"
# import sys
#
# p = Path(sys.argv[1])
#
#
# def parse_folder_recursion(path):
#     for element in path.iterdir():
#         if element.is_dir():
#             print(f"This is folder {element.name}")
#             parse_folder_recursion(element)
#         else:
#             print(f"This is file {element.name}")
#
#
# if __name__ == "__main__":
#     parse_folder_recursion(p)


def if_elif_vs_dict(operator, x, y):
    return {
        "+": lambda: x + y,
        "-": lambda: x - y,
        "*": lambda: x * y,
        "/": lambda: x / y,
    }.get(operator, lambda: "This is not valid operation")()


operator = input("Please set the operator: ")
x = float(input("Please set the x: "))
y = float(input("Please set the y: "))
a = if_elif_vs_dict(operator, x, y)
print(a)
