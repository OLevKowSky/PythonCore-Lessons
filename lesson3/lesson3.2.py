"""Lesson 3. Practical"""


# def modeling(factor, *_, correction):
#     pass
#
# def modeling(factor, _): # з права "_" - змінна ігнорується
#     pass
#
#
# d = {}
#
# for _, value in d:
#
#
# def _hello(): # з ліва "_" - права доступу, "увага"
#     pass
#
# def __hello(): # з ліва "__" - права доступу, не має доступу ззовні, тільки зсередини
#     pass

# def hello():
#     print("Hello")
#
#
# def name(name, hello):
#     h = hello()
#     print(name, hello)
#
#
# name("alisa", hello())

# Recursion

# def count_items(item_list):
#     """Recursion function count items in list."""
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items([1, 2, 3, 4]))
# print(count_items([1, [2, 3], 4]))
# print(count_items([]))

# def is_palindrome(word: str):
#     """Return True if word is Palindrome."""
#     return word == word[::-1]
#
#
# print(is_palindrome("civic"))

# def is_palindrome(word: str):
#     """Return True if word is Palindrome."""
#     if len(word) <= 1:
#         return True
#     else:
#         return word[0] == word[-1] and is_palindrome(word[1:-1])
#
#
# print(is_palindrome("hello"))

# fibonacci - F(n) = F(n-1) + F(n-2)

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# number = 5
#
# for n in range(number):
#     print(fibonacci(n))

# def greet_users(names):
#     for name in names:
#         msg = "Hello, " + name.title()
#         print(msg)
#
# user_names = ["alisa", "bob", "mike"]
#
#
# greet_users(user_names)

def create_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("Please, enter your name: ")
    print("(enter 'q' if you want to quit)")

    f_name = input("First name: ")
    if f_name == "q":
        break

    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = create_formatted_name(first_name=f_name,
                                           last_name=l_name)
    print("Hello, " + formatted_name)