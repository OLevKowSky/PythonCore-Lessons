"""lesson 2.1"""

# if conditions

# age = int(input("How old are you? "))
#
# if age >= 18:
#     print(f"Your {age} is more than 18")
# else:
#     print("Your are not adult")


# debuger

# age = input("How old are you? ")
#
# if type(age) is int:
#
#     if int(age) >= 18:
#         print(f"Your {age} is more than 18")
#     else:
#         print("Your are not adult")
#
# else:
#     print("It is not a int type")


# ternar operator

# number = 7
# message = "Even" if number % 2 == 0 else "Odd"
# print(message)

# number = 7
# message = ""
#
# if number % 2 == 0:
#     print("Even")
# elif number % 2 != 0:
#     print("Odd")
# else:
#     print("Not number")

# your_age = int(input("Please, enter your age: "))
# driving_licence = "You can drive car" if your_age >= 18 else "Sorry "
# print(driving_licence)


# more exsamples

# number = input("Please, enter your number: ")
# number = int(number)
#
# if number > 0:
#     print("It's positive number")
#
# elif number < 0:
#     print("It's negative number")
#
# else:
#     print("This number is zero")

# result = None
#
# if result:
#     print(result)
#
# else:
#     print("Result is None")

# user_email = input("Please, enter your email: ")
#
# if user_email:
#     print(f"Your email is {user_email}")
# else:
#     print("Please, enter your email")


# while loop

# number = 1
#
# while number <= 10:
#     print(number)
#     number += 1


# break

# number = 0
#
# while True:
#
#     print(number)
#
#     if number >= 10:
#         break
#
#     number += 1

# while True:
#
#     user_exit = input().lower()
#     print(user_exit)
#
#     if user_exit == "exit":
#         break


# continue

# number = 0
#
# while number <= 10:
#
#     number += 1
#
#    if not number % 2:
#         continue
#
#     print(number)


# one more exsample

# unconfirmed_users = ["alisa", "bob", "mike"]
# 
# confirmed_users = []
# 
# while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verified users: " + current_user.title())
    confirmed_users.append(current_user)

    print(f"Confirmed users {confirmed_users}")

# for loop

# name = "Alisa is a great girl"
#
# for char in name:
#     print(char)


# loop in list

# list_of_fruits = ["apple", "orange", "tangirene"]
#
# for fruit in list_of_fruits:
#     print(fruit)

# list_of_fruits = ["apple", "orange", "tangirene"]
#
# for fruit in list_of_fruits[1]:
#     print(fruit)


# dict - словник

# student = {"name": "Bob", "age": 20}
# 
# for key in student:
#     print("KEY ", key)

# student = {"name": "Bob", "age": 20}
# 
# for key, value in student.items():
#     print("KEY ", key)
#     print("VALUE ", value)
