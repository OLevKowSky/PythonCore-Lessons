"""Lesson 5. Preperation"""

# STRINGS

# my_string = "Afknnsaluas"

# my_string = """sjnvlnlnfv
# lfnvlnklfnklnvdf
# ljansvjlnklnvlknd
# ljnfljnaskmv"""
# print(my_string)

# my_string = "kmsknvf" \
#     "kmfvklnsflv"\
#
# print(my_string)

# print(f'{2+2}')

# a = 5
# print(f"{a}")

# my_func = lambda: 2 + 2
#
# print(f"{my_func()}")

# print("{} {}".format(1, 2))

# print("{a} {b}".format(b=1, a=2))

# print("{1} {0}".format(1, 2)) # по індексу

# print("{0:d} {0:#b}".format(1, 2))

# print("{:d} {:#b}".format(1, 2))

# print("{:#x} {:#b}".format(1, 2))

# print(hex(1))

# print(f"{hex(1)}")

# print('{:>8}'.format("a"))

# print('{:*^5}'.format("a"))

# print("{:0.5}".format(5.56489567))

# print("{:+0.3}".format(5.56489567))

# REGULAR EXPRESSIONS

# import re

# a = "123"
# result = re.search("\d", a)
# print(result)

# result = re.search("\w", a)
# print(result)

# result = re.search("\s", a)
# print(result)

# result = re.search("\d{3}", a)
# print(result.group())

# result = re.findall("\d", a)
# print(result)

# result = re.search("\d{10}", "hhg0123456789klnklnv")
# print(result)

# result = re.search("0\d{10}", "hhg0123456789klnklnv")
# print(result)

# result = re.search("0\d{10}", "0123456789")
# print(result)

# result = re.search("^\d{10}", "0123456789")
# print(result)

# result = re.search("^0\d{9}", "0123456789fadfgs")
# print(result)

# result = re.search("^0\d{9}$", "0123456789fadfgs")
# print(result)

# result = re.search("^0\d{9}$", "0123456789")
# print(result)

# result = re.search("^0\d{9}\s{3}\w{5}$", "0123456789   klhvl")
# print(result)

# result = re.search("^\+38\(\d{3}\)\d{7}", "+38(068)1231212")
# print(result)

# result = re.search("^\+38.\d{3}.\d{7}", "+38(068)1231212")
# print(result)

# result = re.search("^\+38.\d{3}.\d{3}.\d{2}.\d{2}", "+38(068)123-12-12")
# print(result)

# print(re.search("^[a-z0-9]+[@]\w+[.]\w{2,3}", "asd@gmail.com"))

# print(re.search("^[a-z0-9._]+[@]\w+[.]\w{2,3}", "asd.123_123@gmail.com"))

# logs = """vasf10.124.15.38bvfjlbvjlb
# alsjk104.13.16.59bvjkbajksb
# aklb123vkasbvk12asb
# fjlsdb138.123.78.1kjbfjabs
# ihsbhbvfb"""
#
# ip_address = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", logs)
# print(ip_address)

# logs = """FirstName: favjksbfuvbru LastName: wfjivnjoefvn Age: 12 Address: ojefvnjowefnvj"""
#
# user_input = input("Field name: ")
#
# result = re.findall("LastName:\s\w+\s", logs)
# print(result)

# result = re.findall(f"{user_input}:\s\w+\s?", logs)
# print(result)

# user_pattern = '\d{10}'
# string = "1236515618125161"
#
# def findall(pattern, string):
#
#     patterns = {'\d': lambda a: a.isdigit()}  # patterns = {'\d': str.asdigit}
#
#     for key in patterns:
#
#         if pattern.startswith(key):
#             pattern_key = key
#             n_times = int(pattern[pattern.find("{") + 1 : pattern.find("}")])
#
#     result_string = ""
#
#     for char in string:
#
#         if patterns[pattern_key](char):
#
#             result_string += char
#         else:
#             result_string = ""
#
#         if len(result_string) == n_times:
#            return result_string
#
#
# print(findall(user_pattern, string))

# my_string ="sbkbjkbv.oasnnfni*fnvkfnv_ifnvkfnv" # result == ["sbkbjkbv", "oasnnfni", "fnvkfnv", "ifnvkfnv"]
# patterns = ["*", ".", "_"]
#
# for char in my_string:
#     if char in patterns:
# продовжити

# import re
# "[a-zA-Z]"
# print(re.match('[a-zA-Z0-9._]', "a"))
# print(re.match('[a-zA-Z0-9._]', "aasd"))
# print(re.match('^[a-zA-Z0-9._]$', "aasd"))
# print(re.fullmatch('[a-zA-Z0-9._]', "aasd"))
# print(re.fullmatch('[a-zA-Z0-9._]+', "aasd"))
# print(re.fullmatch('[a-zA-Z0-9._]{3, 10}', "aasd"))
# print(re.fullmatch('[a-zA-Z0-9._]{3, 10}', "sd"))
# print(re.fullmatch('[a-zA-Z0-9._]{3, 10}', "vkasvdhausdcoasbv"))
# print(re.fullmatch('[a-zA-Z0-9._]{3, 10}', "b._asdqwe"))
# print(re.fullmatch('[a-zA-Z0-9._]{3, 10}', "b._asdqwe!"))

from re import fullmatch

RE_LOGIN = "[a-zA-Z0-9._]{3,10}"
RE_PWD = "[a-zA-Z0-9._!&#]{8,15}"

users_db = {}

def check_input(reg_exp, user_input):

    if not fullmatch(reg_exp, user_input):
        raise ValueError(f"Input should be {reg_exp}")

    return True


def check_if_login_exists(login):

    global users_db

    return False if login in users_db else True


def register():

    login_check_result = False
    pwd_check_result = False

    while True:

        if not login_check_result:
            user_login = input('New Login: ')
            login_check_result = check_if_login_exists(user_login)
            continue  

        try:
            login_check_result = check_input(RE_LOGIN, user_login)
        except ValueError as error:
            print(error)

        if not pwd_check_result:
            user_pwd = input("New password: ")

        try:
            pwd_check_result = check_input(RE_PWD, user_pwd)
        except ValueError as error:
            print(error)

        return user_login, user_pwd


def login():

    global users_db

    user_login = input('Login: ')
    user_pwd = input("Password: ")

    try:
        return True if users_db[user_login]["pwd"] == user_pwd else False
    except KeyError:
        return False


while True:

    action = input("Register or login:")

    if action == "register":
        user_login, user_pwd = register()
        users_db[user_login] = {"pwd": user_pwd}
        print(users_db)

    elif action == "login":
        if login():
            print("Welcome")
        else:
            print("Try again")

