"""Lesson 5.0. Additional matirials"""

# Методи пошуку в строках "find" та "index"

# files = ["video.avi", "audio.mp3", "document.doc", "folder"]
#
# for file in files:
#     indx = file.find(".")
#     if indx != -1:
#
#         suffix = file[indx+1:]
#         print(f"File: {file} Index: {indx} Suffix: {suffix}")
#     else:
#         print(f"File: {file} Suffix: not found")
#
# for file in files:
#     try:
#         indx = file.index(".")
#         suffix = file[indx + 1:]
#         print(f"File: {file} Index: {indx} Suffix: {suffix}")
#     except ValueError:
#         print(f"File: {file} Suffix: not found")

#
# files = ["video.avi", "audio.mp3", "document.doc", "folder", "backup.tar.gz"]
#
# for file in files:
#     try:
#         indx = file.index(".")
#         suffix = file[indx + 1:]
#         print(f"File: {file} Index: {indx} Suffix: {suffix}")
#     except ValueError:
#         print(f"File: {file} Suffix: not found")
#
# for file in files:
#     try:
#         indx = file.rindex(".")
#         suffix = file[indx + 1:]
#         print(f"File: {file} Index: {indx} Suffix: {suffix}")
#     except ValueError:
#         print(f"File: {file} Suffix: not found")

# "split" та "join"

# text = "first sentence. Second sentence! Third sentence?"
# sentences = text.split(".")
# print(sentences)

# import re
#
# text = "first sentence. Second sentence! Third sentence?"
# sentences = re.split("[\.\!\?]", text)
# print(sentences)

# import re
#
# text = "first sentence.\nSecond sentence!\nThird sentence?"
# print(text)
#
# sentences = text.split("\n")
# print(sentences)
#
# new_text = " ".join(sentences)
# print(new_text)

# строковий метод "format"

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# header = "|{:^15}|{:^15}|{:^15}|".format("int", "int^2", "int^3")
# separator = "-"*len(header)
# body = ""
# for num in numbers:
#     body += "|{:^15}|{:^15}|{:^15}|\n".format(num, num**2, num**3)
# table = "\n".join([separator, header, separator, body, separator])
# print(table)
#
# header = "|{:^15}|{:^15}|{:^15}|{:^15}|".format("int", "dex", "oct", "bin")
# separator = "-"*len(header)
# body = ""
# for num in numbers:
#     body += "|{0:^15d}|{0:^15x}|{0:^15o}|{0:^15b}|\n".format(num)
# table = "\n".join([separator, header, separator, body, separator])
# print(table)

# строковий метод "translate"

# trans_map = {ord("Я"): "Ya", ord("н"): "n", ord("а"): "a", ord("о"): "o"}
# ukr_name = "Яна"
# lat_name = ukr_name.translate(trans_map)
# print(ukr_name, '=', lat_name, sep = " ")
#
# text = "Hello Wоrld"
# indx = text.find("World")
# new_indx = text.translate(trans_map).find("World")
# print(new_indx)
