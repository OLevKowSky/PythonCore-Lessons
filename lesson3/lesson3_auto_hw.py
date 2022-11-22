# 1

# def greeting():
#     print("Hello world!")
#
#
# greeting()


# 2

# def invite_to_event(username):
#     return f"Dear {username}, we have the honour to invite you to our event"
#
#
# username = input("Enter your full name: ")
#
# print(invite_to_event(username))


# 3

# base_rate = 40
# price_per_km = 10
# total_trip = 0
#
#
# def trip_price(path):
#     global total_trip
#     trip_price = base_rate + path * price_per_km
#     total_trip = total_trip + 1
#     return trip_price
#
#
# trip_price(10)
# print(trip_price)


# 4 код, який прийняло як правильний, але не вирішується у VSC

# def discount_price(price, discount):
#     discount_price = price * (1 - discount)
#     return discount_price
#
#     def apply_discount():
#         nonlocal price
#         price = input("Enter the price of item: ")
#
#     apply_discount()
#     return price
#
#
# discount_price(100, 0.1)


# 5


# 6

# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     else:
#         return " " * ((length - len(string)) // 2) + string
#
#
# print(format_string("aaaa", 4))


# 7.1 Моє рішення

# def first(size, *args):
#     count_args = 0
#     for arg in args:
#         count_args += 1
#
#     print(size, count_args)
#
#
# first(5, "first", "second", "third")
#
#
# def second(size, **comments):
#     count_comments = 0
#     for comment in comments:
#         count_comments += 1
#
#     print(size, count_comments)
#
#
# second(3, comment_one="first", comment_two="second", comment_third="third")

# 7.2 код, який прийняло як правильний

# def first(size, *args):
#     return size + len(args)
#
#
# print(first(5, "first", "second", "third"))
#
#
# def second(size, **comments):
#     return size + len(comments)
#
#
# print(second(3, comment_one="first", comment_two="second", comment_third="third"))


# 8

# def cost_delivery(quantity, *_, discount=0):
#
#     cost_delivery = 0
#     if quantity == 1:
#         cost_delivery = 5
#     else:
#         cost_delivery = (5 + ((quantity - 1) * 2))
#     cost_delivery = cost_delivery * (1 - discount)
#     return cost_delivery
#
#
# print(cost_delivery(2, 1, 2, 3))

# 10
