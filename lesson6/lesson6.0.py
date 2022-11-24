"""Lesson 6.0."""

# file = open('lesson6.0.1.txt', mode = "r")
# print(file.name)

# file.close()
# print(file.closed)

# info = file.read(1)
# print(info)

# info = file.read(1024)
# print(info)
#
# info = file.read(1024)
# print(info)

# info = file.readline() # не прийнято змішувати
# print(info)
#
# info = file.read(1024)
# print(info)

# info = file.readline()
# print(info)
#
# info = file.readline(1024)
# print(info)

# while True:
#     data = file.read(2)
#     print(data)
#
#     if not data:
#         break

# for line in file:
#     print(line)

# with open('lesson6.0.1.txt', mode = "r") as file:
#     file.read()
#     print(file.closed)

# file.close()
# print(file.closed)

# with open('lesson6.0.2.txt', mode = "w") as file:
#     file.write("vnkfndalks\njfnajdbj\njafjbwjf")

# with open('lesson6.0.2.txt', mode = "a") as file:
#     file.write("lmlnmyer\nksndmasv\nqwefv")

# with open('test.pdf', mode = "rb") as file:
#     print(file.read(10))

# with open('test.bin', mode = "wb") as file:
#     file.write(b'asd')

# with open('lesson6.0.1.txt', mode="r") as file:
#     file.seek(3) # зміщує курсор в право на певну кількість виступів
#     print(file.read(3))

# with open('lesson6.0.1.txt', mode="r") as file:
#     print(file.tell())
#     print(file.read(2))
#     print(file.tell())

# with open('lesson6.0.1.txt', mode="r") as file:
#     data = file.read()
#
# data = data.replace("l", "")
#
# with open('lesson6.0.1.txt', mode="w") as file:
#     file.write(data)

# with open('lesson6.0.1.txt', mode="a+") as file:
#     file.read()
#     file.write(data.replace("l", ""))

# from csv to html

# NAME = "Contact_Name"
# URL = "Website"
#
# list_element = "    <li><a href={url}>{name}</a></li>\n"
#
# with open("Business_List.csv", "r") as file:
#
#     with open("Business_List.html", "a") as html:
#
#         html.write("<ul>\n")
#
#         headers = []
#
#         for line in file:
#
#             data = line.split(",")
#             data[-1] = data[-1][:-1]
#
#             if not headers:
#
#                 headers = data
#                 name_index = headers.index(NAME)
#                 url_index = headers.index(URL)
#
#                 continue
#
#             name = data[name_index]
#             url = data[url_index]
#
#             html.write(list_element.format(url=url, name=name))
#
#         html.write("</ul>\n")
