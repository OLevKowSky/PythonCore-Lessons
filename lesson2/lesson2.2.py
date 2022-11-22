"""lesson 2.2"""

# Try Except # Handling Error

# x = 2
# y = 0
# try:
#     result = x / y
#     print(f"Result is equal {result}")
#
# except ZeroDivisionError:
#     print("You can't devide to zero")
# else:
#     print("All is OK")
# finally:
#     print("Its a finally block")

# for loop

# people = ["alisa", "bob", "mike", "carolina"]
# print("People ", people[0])

# print("People ", people[0][1])

# for human in people:
#    print("Human", human)

# for human in people:
#     print(human.title() + ", your great person")

# for value in range(1, 10, 2):
#     print(value)

# squares = []
#
# for value in range(1, 11):
#     square = value**2
#     squares.append(square)
#
# print("Squares :", squares)

# squares = []
#
# for value in range(1, 11):
#     square = value**2
#     squares.append(square)
#
#     print("Squares :", squares)

# cars = ["bmw", "seat", "audi", "toyota", "subaru"]
#
# for car in cars:
#     if car == "bmw":
#         print("Car upper", car.upper())
#     else:
#         print("Car title", car.title())

# request_topping = "pineapple"
# if request_topping != "orange":
#     print("you got prize")

# request_topping = ["mushrooms", "tomatos", "pizza"]
# if "mushrooms" in request_topping:
#     print("yes")

# word = "Dmytro"
# for w in word:
#     if "m" in w:
#         print("hello")

# available_toppings = ["mushrooms", "olives", "peppers", "pepperoni"]
#
# requested_toppings = ["mushrooms", "cheese", "tomatos"]
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Added " + requested_topping)
#     else:
#         print("Sorry " + requested_topping)

# favorite_languages = {
#    "dmytro": "python",
#    "natali": "c",
#    "denis": "ruby",
#    "nataly": "python"
# }

# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title())

# for name in favorite_languages:
#     print(name.title() + "'s favorite language is " )

# for language in favorite_languages.values():
#     print(language.title() + " language")

# favorite_languages = {
#     "dmytro": ["python", "ruby"],
#     "natali": ["c", "c++"],
#     "denis": ["ruby"],
#     "nataly": ["python", "go"]
# }

# for name, languages in favorite_languages.items():
#     print(name.title() + "'s favorite language are ")
#     for language in languages:
#         print(" " + language.title())

# users = {
#     "Boby": {
#         "first_name": "Bob",
#         "last_name": "File",
#         "location": "Las-Vegas"
#     },
#     "Alisa": {
#         "first_name": "Alisa",
#         "last_name": "Erickson",
#         "location": "New-York"
#     }
# }
#
# for username, user_info in users.items():
#     print("Username " + username)
#     full_name = user_info["first_name"] + " " + user_info["last_name"]
#     location = user_info["location"]
#     print("Full name: " + full_name)
#     print("Location: ", location)

# while loop

# current_number = 1
#
# while current_number <= 6:
#     print(current_number)
#     current_number += 1

# message = "Tell something I will repeate: "
# message += "Enter 'quit' for end "
# promt = ""
# 
# while promt != 'quit':
#     promt = input(message)
#     print(promt)

# promt = "Please, enter the name of city you would have visited "
# promt += "For end, please, input 'quit' "
# 
# while True:
#     city = input(promt)
#     if city == 'quit':
#         break
#     else:
#         print("I would love to go to " + city.title())

# word = "Restaurant"
# 
# for char in word:
#     if char == "u":
#         continue
#     print(char)

names = ["alisa", "bob", "mickle"]

for name in names:
    if name == "bob":
        break
    print("All company done")