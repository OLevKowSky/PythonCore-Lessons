"""Lesson 5.2."""

# REGEX

import re

# text = "The same the new text by Alisa the"
# t = re.findall("the", text, flags=re.I)
# print(t)


# def some_pattern(text):
#    return re.findall("the", text, flags=re.I)
# 
#
# print(some_pattern(text))


# def search_pattern(text):
#     return re.search("the", text)
# 
# 
# print(search_pattern(text))


# def search_pattern(text):
#     span = re.search("the", text)
#     return span.span()
# 
#
# print(search_pattern(text))


# t = re.match("the", text)
# print(t)

# is_match = re.match("the", text, flags=re.I)
# 
# if is_match:
#     print(f"{is_match.group()} appers at {is_match.span()}")
# else:
#     print(is_match)

# "sub" змінює відповідний підрядки на ..., наприклад замінити пін на *** 

# text = "my password is 123456"
# 
# change = re.sub("1", "*", text)
# print(change)

# text = "Hello, my, name, is! Alisa"
#
# s= re.split(",", text)
# print(s)

# text = "Hello! We are good devs with_80 level @"
#
# pattern = r"\w" # будь-який буквенно-цифровий символ
# p = re.findall(pattern, text)
# print(p)

# pattern = r"\W" # ве що не є "\w"
# p = re.findall(pattern, text)
# print(p)

# pattern = r"\d" # цифра від 0 до 9
# p = re.findall(pattern, text)
# print(p)

# pattern = r"\D" # нецифровий символ
# p = re.findall(pattern, text)
# print(p)

# pattern = r"\s" # пробіли
# p = re.findall(pattern, text)
# print(p)

# pattern = r"\S" # все що не є пробілом
# p = re.findall(pattern, text)
# print(p)

# pattern = r"[a-fA-F]"
# p = re.findall(pattern, text)
# print(p)

# pattern = r"[^a-fA-F]" # поверне все, крім [a-fA-F]
# p = re.findall(pattern, text)
# print(p)

# text = "hello hello ago gelloo helloooohgdfdgfaug"
#
# pattern = r"hello+" # ["hello", "hello", "helloooo"] 1 або більше разів
# p = re.findall(pattern, text)
# print(p)

# pattern = r"hello*" # ["hello", "hello", "helloooo"] 0 або більше разів
# p = re.findall(pattern, text)
# print(p)

# pattern = r"hello?" # ["hello", "hello", "hello"] 0 або 1 раз
# p = re.findall(pattern, text)
# print(p)

# text = "10.5% taxes in 2022 and in 2023 will be increse"
# 
# pattern = r"\d{4}" # виводить цифри з 4ма символами
# p = re.findall(pattern, text)
# print(p)

# {min, max}

# text = "alisa@gmail.com, bob@mail.us, mike@web.biz"
#
# pattern = r"\.\w{2,5}" # ['.com', '.us', '.biz']
# p = re.findall(pattern, text)
# print(p)

# text = "Hello! We are good devs with_80 level @"
#
# pattern = r"\w{5,}" # {min,} # ['Hello', 'with_80', 'level']
# p = re.findall(pattern, text)
# print(p)

# text = "100 000 items"
#
# pattern = r"^\d\d" # ['10']
# p = re.findall(pattern, text)
# print(p)

# pattern = r"\w{3}$" # ['ems']
# p = re.findall(pattern, text)
# print(p)

# Groups

# text = "Ilona work on phone"
# 
# pattern = r"(.o.)" # ['lon', 'wor', ' on', 'hon']
# p = re.findall(pattern, text)
# print(p)

text = "Ths @alisa email alisa@gmail.com"

pattern = r"(\w+)@(\w+)\.(\w+)\b"
p = re.search(pattern, text)
# print(p)
# print(p.group(0)) # повний збіг паттерну
# print(p.group(1)) # перший збіг паттерну
# print(p.group(2)) # gmail
print(p.group(3)) # com
