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
