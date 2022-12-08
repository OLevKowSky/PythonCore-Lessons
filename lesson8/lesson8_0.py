"""Lesson 8_0"""

# 
# import collections
# 
# named_tuple = collections.namedtuple("tuple", ["first_name", "last_name", "age"])
# print(named_tuple)
# 
# named_tuple.first_name = "asd"
# print(named_tuple.first_name)

# defaultdict
# 
# from collections import defaultdict
# 
# abc = defaultdict(lambda: 1, {"a": 1})
# abc["b"]
# print(abc)

# datetime
#
# from datetime import datetime
#
# current_time = datetime.now()
# print(current_time)
#
# a = datetime(year=2022, month=1, day=4)
# print(a)
# 
# a = datetime.strptime("2022/02/17 18:53", "%Y/%m/%d %H:%M")
# print(a)
# 
# a = datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M")
# print(a)

# import time
#
# start = time.time()
# a = time.time() - start
# print(a)

# random

# import random
#
# a = random.random()
# print(a)

# a = random.randint(0, 100)
# print(a)

# abc = [1, 2, 3, 4, 5]
# a = random.choice(abc)
# print(a)

# abc = [1, 2, 3, 4, 5]
# a = random.choices(abc, k=3)
# print(a)

# abc = [1, 2, 3, 4, 5]
# random.shuffle(abc)
# print(abc)

# array

# from array import array
#
# int_array = array("i", range(0, 10000))
# for i in int_array:
#     print(i)
#     break

# from array import array
# import time
#
# start = time.time()
# int_array = array("i", range(0, 1000000))
# print(time.time() - start)
#
# start = time.time()
# int_list = list(range(0, 1000000))
# print(time.time() - start)
#
# start = time.time()
# [i**2 for i in int_array]
# print(time.time() - start)
#
# start = time.time()
# [i**2 for i in int_list]
# print(time.time() - start)

# from array import array
# import pickle
# import time
#
# start = time.time()
# int_array = array("i", range(0, 1000000))
# print(time.time() - start)
#
# start = time.time()
# int_list = list(range(0, 1000000))
# print(time.time() - start)
#
# start = time.time()
# pickle.dumps(int_array)
# print(time.time() - start)
#
# start = time.time()
# pickle.dumps(int_list)
# print(time.time() - start)

# zlib

# import zlib
# 
# a = zlib.compress(b"jasdlkvb;abkj;vbasdvb")
# print(a)

# import zlib
# 
# a = zlib.compress(b"jasdlkvbsabkjdvbasdvb")
# with open("test8_0.zip", "bw") as file:
#     file.write(a)

# import zlib
# 
# a = zlib.compress(b"jasdlkvb;abkj;vbasdvb")
# with open("test8_0.zip", "br") as file:
#     print((file.read()))

import zlib

a = zlib.compress(b"jasdlkvb;abkj;vbasdvb")
with open("test8_0.zip", "br") as file:
    print(zlib.decompress(file.read()))
