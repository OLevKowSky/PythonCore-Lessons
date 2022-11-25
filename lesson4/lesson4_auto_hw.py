# 1

# def amount_payment(payment):
#
#    amount_payment = 0
#     for sum in payment:
#         if sum >= 0:
#             amount_payment = amount_payment + sum
#
#     return amount_payment
#
#
# print(amount_payment([2, -3, 4]))

# 2

# def prepare_data(data):
#
#     data.sort()
#     data.pop(0)
#     data.pop(-1)
#     return data
#
#
# print(prepare_data([1, 2, 3, 4, 5]))

# 3

# def format_ingredients(items):
#     if not items:
#         return ""
#     if len(items) == 1:
#         recipe = items[0]
#     else:
#        recipe = ", ".join(items[:-1:]) + " and " + items[-1]
#     if not recipe:
#         return items[0]
#     return f"{recipe}"
#
#
# print(format_ingredients(["2 eggs"]))

# 4

# def get_grade(key):
#     ECTS = {
#         "F": 1,
#         "FX": 2,
#         "E": 3,
#         "D": 3,
#         "C": 4,
#         "B": 5,
#         "A": 5
#         }
#     i = ECTS.get(key, )
#     return i
#
#
# print(get_grade("F"))
#
#
# def get_description(key):
#     ECTS = {
#         "F": "Unsatisfactorily",
#         "FX": "Unsatisfactorily",
#         "E": "Enough",
#         "D": "Satisfactorily",
#         "C": "Good",
#         "B": "Very good",
#         "A": "Perfectly"
#     }
#     i = ECTS.get(key, )
#     return i
#
#
# print(get_description("A"))

# 5

# def lookup_key(data, value):
#
#     result = []
#     for key, val in data.items():
#         if val == value:
#             result.append(key)
#     return result
#
#
# print(lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2))

# 6

# def split_list(grade):
#
#     list1 = []
#     list2 = []
#     try:
#         avg = sum(grade) // len(grade)
#         for i in grade:
#             if i <= avg:
#                 list1.append(i)
#             else:
#                 list2.append(i)
#         tuple = (list1, list2)
#     except ZeroDivisionError:
#         tuple = ([], [])
#     print(tuple)
#     return tuple
#
# split_list([1, 12, 3, 24, 5])

# 7

# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9,
# }
#
#
# def calculate_distance(coordinates):
#
#     distance = 0
#     i = 0
#     list = []
#     if len(coordinates) <= 1:
#         return 0
#
#     for i in range(0, len(coordinates)-1):
#         if coordinates[i] > coordinates[i+1]:
#             list.append((coordinates[i+1], coordinates[i]))
#         else:
#             list.append((coordinates[i], coordinates[i+1]))
#
#     for k in list:
#         distance += points.get(k)
#     return distance
#
#
# print(calculate_distance([0, 1, 3, 2, 0, 2]))

# 8

# def game(terra, power):
#
#     get_power = power
#     for t in terra:
#         for p in t:
#             if p <= get_power:
#                 get_power += p
#             else:
#                 get_power += 0
#                 break
#     return get_power
#
#
# print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))

# 9

# def is_valid_pin_codes(pin_codes):
#
#     flag = False
#     if len(pin_codes) == len(set(pin_codes)):
#         for i in pin_codes:
#             if i and len(i) == 4 and isinstance(i, str) and i.isnumeric():
#                 flag = True
#             else:
#                 flag = False
#         return flag
#     else:
#         return False
#
#
# print(is_valid_pin_codes(['1101', '9034', '0011', '1101']))

# 10
