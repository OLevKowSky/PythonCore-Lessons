"""Lesson 5. STRINGS"""

# n = [2, 1, 5, 7]
# s = sorted(n) # функція повертає новий відсортований список
# print(s)

# s1 = n.sort() # метод не повертає, він змінює список
# print(s)

# додавання

# s = "some string"
# n = "new string"
#
# res_string = s + " " + n
# print(res_string)

# створення копій рядка

# s = "some string "
#
# res_str = s * 5
# print(res_str)

# оператори

# s = "some string"
#
# res_str = "some" in s
# print(res_str) ## True

# s = "some string"
#
# res_str = "some" not in s
# print(res_str) ## False

# s = "some string"
#
# res_str = "abc" in s
# print(res_str) ## False

# s = "some string"
#
# res_str = "abc" not in s
# print(res_str) ## True

# value = ord("s")
# value2 = ord("S")
# print(value)
# print(value2) # повертає в десятковій системі числення з таблиці ASCI

# value_utf = ord("$")
# print(value_utf) # повертає з UNICODE(UTF)

# value = chr(115)
# print(value) # зворотня операція від ord()

# s = "My name is Alisa"
# print(len(s)) # довжина строки

# n = 4
# print(type(n))
# s = str(n)
# print(type(s)) # перетворення в строку

# s = "somestring"
# print(s[0])
# print(s[-1])
# print(s[len(s)-1]) # як доступитися до строки

# s = "somestring"
# print(s[3:7]) # зрізи

# s = "somestring"
# print(id(s)) # викликає id строки

# методи виведення строки

# name = "Alisa"
# print(f"My name is {name}")

# name = "Alisa"
# print("My name is {name}".format(name=name))

# name = "Alisa"
# print(f"My name is \" {name}") # екранування

# number = 321.54894512316484
# print("number: {:0.5}".format(number))

# name = "Alisa"
# surname = "Simpson"
# print("My name is {name}, {surname}".format(name=name, surname = surname))

# name = "Alisa"
# surname = "Simpson"
# print("My name is {surname}, {name}".format(name=name, surname = surname))

# інші методи

# s = "foobar"
# res = s.replace("b", "c")
# print(res) # метод replace

# s = "foo bar baz"
# res_str = s.capitalize()
# print(res_str)

# s = "Foo@GMAIL.com"
# res = s.lower() # по символах
# print(res)
# res2 = s.casefold() # по кейсах
# print(res2)

# s = "foo bar baz"
# res = s.title()
# print(res)

# s = "foo bar baz"
# res = s.upper()
# print(res)

# s = "foo bar baz"
# res = s.count("o")
# print(res)

# s = "foobarbaz"
# res = s.endswith("baz")
# print(res)

# s = "foobarbaz"
# res = s.startswith("foo")
# print(res)

# s = "foo bar baz"
# res = s.find("bar")
# print(res)

# s.isalpha()
# s.isdigit()
# s.isalnum()

# name = "  Alisa   "
# n = "Alisa"
# print(n == name)
#
# res = name.strip() # також є lstrip(зліва) та rstrip(справа)
# print(res == n)

# http = "https://www.google.com"
# print(http.lstrip("/:pth"))
# print(http.lstrip("//:https"))

# l = ["foo", "bar", "baz", "abc"]
#
# res = ", ".join(l)
# print(res)

# http = "www.google.com"
# res = http.split(".")
# print(res)

# s = "foo...bar"
# res = s.rsplit(".")
# print(res)

# s = "foo\tbar"
# res = s.rsplit()
# print(res)

# print("My\n nam\re is\t Alisa\r\n. I'm developer")

# s = "foobar"
# res = bytes(s, "utf-8")
# print(res)

# s = "foobar"
# l = [1, 2, 3, 4]
# res = bytes(s, "utf-8")
# res_l = bytes(l)
#
# print(res)
# print(res_l)

# Regular expressions
#regex

# reg = r"[A-z][0-9][]\@$%"

import re

s = "foobar1234"

print(re.search("1234", s))
x = re.search("[0-9]", s)
print(x)
x1 = re.search("[0-9][0-9][0-9][0-9]", s)
print(x1)



