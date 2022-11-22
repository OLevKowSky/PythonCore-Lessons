"""Lesson 6.1."""

# test_handler = open("test6.1.txt")
# print(test_handler)

# Error handling
# test_handler = open("test6.2.txt")
# print(test_handler)

# test_handler = open("test6.1.txt")

# for line in test_handler:
#     print(line)

# for line in test_handler:
#     print(repr(line))

# for line in test_handler:
#     print(line, end = ",")

# for line in test_handler:
#     line = line.rstrip()
#     print(repr(line))

# Write to file
# "w" - write
# "a" - add to existance file
# "x" - create file and return error if file exist

# write_to_file = open("test6.2.txt", "w")
# write_to_file.write("Today is a good day for learning Python")
# write_to_file.close()

# write_to_file = open("test6.2.txt", "w")
# write_to_file.write("Today is a good day for learning Django")
# write_to_file.close()

# write_to_file = open("test6.2.txt", "a")
# write_to_file.write("Today is a good day for learning Python")
# write_to_file.close()

# write_to_file = open("test6.2.txt", "x")
# write_to_file.write("Today is a good day for learning Python")
# write_to_file.close()

# write_to_file = open("test6.3.txt", "x")
# write_to_file.write("Today is a good day for learning Flask")
# write_to_file.close()

# обробка помилки

# fname = input("Please enter the file name: ")
# try:
#     file_handler = open(fname)
# except:
#     print("File not found: ", fname)
#     exit()
#
# count = 0
#
# for w in file_handler:
#     count += 1
# print("There are ", count, " lines in ", fname)

# Сontext mamager

# with open("test6.3.txt", "rb") as reader:
#     print(reader.read())

# with open("test6.3.txt", "rb") as reader:
#     print(reader.read(2))
#     print(reader.read(2))
#     print(reader.read(2))
#     print(reader.read(2))
#     print(reader.read(5))

# with open("test6.3.txt", "r") as reader:
#     line = reader.readline()
#     while line != "":
#         print(line, end="")
#         line = reader.readline()

# with open("test6.3.txt", "r") as reader:
#     for line in reader.readlines():
#         print(line, end="")

# .write(string)
# .writelines(seq)

# with open("test6.3.txt", "r") as reader:
#     lorem_lines = reader.readlines()
#
# with open("test6.3_reverse.txt", "w") as writer:
#     for lorem in reversed(lorem_lines):
#         writer.write(lorem)

# with open("test6.3.txt", "rb") as reader:
#     print(reader.readline())

# Open image

# with open("gomer.png", "rb") as byte_reader:
#     print(byte_reader.read(2))

# with open("test6.3.txt", "a") as a_writer:
#     a_writer.write("\nAdd new text")

# first_path = "test6.3.txt"
# path_to_write = "test6.4.txt"
#
# with open(first_path, "r") as reader, open(path_to_write, "w") as writer:
#     test_read = reader.readlines()
#     writer.writelines(test_read)
