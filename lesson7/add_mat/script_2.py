# from script_1 import get_length, math # 1й варіант
#
#
# get_length(90)
# print(math.pi)


# import script_1 # 2й варіант
#
#
# script_1.get_length(70)


from script_1 import math, get_length as get_length_by_diameter # alias


def get_length(r):
    length = math.pi * r
    print(f"Radius = {r} Length = {length}")

get_length_by_diameter(180)
get_length(90)
print(math.pi)