"""Lesson7"""

# from random import choice
# choice()

# import my_module  # 1й варіант імпорту функції
#
#
# print(dir(my_module)) # показує, які об'єкти є в модулі (що зберігається в модулі)
#
# my_module.test_function()  # виклик функції

# import my_module
#
#
# print(dir(my_module))
#
#
# def test_function():
#
#     my_module.test_function()

# from my_module import test_function # 2й варіант імпорту функції
#
# test_function()

# from my_module import test_function as test # використання псевдоніму, як в менеджері контексту
#
# test()

# import my_module as m
#
# m.test_function()

# import sys
# print(sys.builtin_module_names)  # вивід всіх вбудованих(builtin) модулів
#
# print(sys.path) # показує порядок пошуку модулів

# from my_module import * # імпортує всі об'єкти з модулю, крім тих що починаються з "_"
#
# test_function()

# from package import my_module # приклади імпорту з пакету модулів
# import package.my_module
# from package.my_module import test_function

# import sys # конфігурація під різні версії
#
# if sys.version_info[0] < 3:
#     import module_for_python_2 as module_for_python
# else sys.version_info[0] == 3.8:
#     import mudule_for_python_3 as module_for_python
#
# module_for_python

# virtual environment

# python -m venv lesson7\my-project\virtual-venv
# lesson7\my-project\virtual-venv\Scripts\activate
# pip list
# pip install flask
# pip list
# deactivate

# для setup.cfg 

# https://choosealicense.com/
# https://semver.org/
