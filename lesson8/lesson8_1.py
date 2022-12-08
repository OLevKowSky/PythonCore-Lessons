"""Lection 8_1"""

# urllib

# from urllib.request import urlopen
#
# page = urlopen("https://www.apple.com/")
#
# content = page.read()
#
# print(page.headers)
# print("")
# print(content)

# dis

# import dis
#
# def greet(name):
#     print(f"Hello {name}")
#
#
# def test(number):
#     return(str(number) + str(number))
#
#
# dis.dis(greet)
#
# dis.dis(test(2))

# pip install emoji

# from emoji import emojize
#
# print(emojize(":thumbs_up:"))

# collections

# from collections import namedtuple

# Point = namedtuple("Point", ["x", "y"])
#
# point = Point(2, 5)
#
# print("point", point)
#
# print("point x", point.x)
# print("point y", point.y)
# print("point indx", point[0])

# generator expression

# Point = namedtuple("Point", (field for field in "xy")) # in ["apple", "orange"]
# print(Point(2, 5))

# Human = namedtuple("Employee", "name position", defaults=["Python developer"])
#
# human = Human("Alisa")
# print(human)
#
# print(human._asdict())

# Human = namedtuple("Employee", "name position", defaults=["Python developer"])
# human = Human("Alisa")
# human = human._replace(position="Ruby developer")
# print(human)

# deque

# from collections import deque

# ticket_queue = deque()
# print(ticket_queue)
#
# ticket_queue.append("Alisa")
# ticket_queue.append("Bob")
# ticket_queue.append("Dmytro")
#
# print(ticket_queue)
#
# one = ticket_queue.popleft()
# print(one)
# two = ticket_queue.popleft()
# print(two)
# three = ticket_queue.popleft()
# print(three)

# recent_pages = deque(["main_page", "shop", "order"], maxlen=3)
#
# recent_pages.appendleft("cart")
# print(recent_pages)

# OrderedDict

# from collections import OrderedDict

# employees = OrderedDict()
#
# employees["developer"] = "1000-2000"
# employees["qa"] = "500-1000"
# employees["pm"] = "1500-2500"
# employees["ba"] = "2000+"
#
# for empl, salary in employees.items():
#     print(empl, "->", salary)

# letters = OrderedDict(b=2, d=4, a=1, c=3)
# print(letters)
# letters.move_to_end("b")
# print(letters)

# cart = {"toys": "cars", "color": "orange"}
#
# # print(cart["items"]) # KeyError: 'items'
#
# cart.setdefault("items", "2")
# print(cart)

# cart = {"toys": "cars", "color": "orange"}
# 
# print(cart.get("items", 2))
# print(cart)

# defaultdict

# from collections import defaultdict

# cars = defaultdict(int)
#
# # print(cars)
#
# cars["mersedes"]
# # print(cars)
#
# cars["mersedes"] +=1
# cars["audi"] +=1
# cars["mersedes"] +=1
# cars["audi"] +=1
# cars["mersedes"] +=1
#
# print(cars)

# cars = [
#     ("mercedes", "s600"),
#     ("mersedes", "G"),
#     ("mersedes", "A"),
#     ("audi", "a100"),
#     ("audi", "a8")
# ]
#
#
# cars_sallon = defaultdict(list)
#
# for car, model in cars:
#     cars_sallon[car].append(model)
#
# print(cars_sallon)

# ChainMap

from collections import ChainMap

cmd_proxy = {} # User doesn't provide a proxy
dev_proxy = {"proxy": "proxy.dev.com"}
prod_proxy = {"proxy": "proxy.prod.com"}

configuration = ChainMap(cmd_proxy, dev_proxy, prod_proxy)
configuration ["proxy"]

print(configuration)
