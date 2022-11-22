"""additional  lesson"""

# from pathlib import Path
# from sys import argv
#
## path = r"D:\\Education\\Programing\\Python_education\\test0"
#
# def read_folder(path: str) -> None:
#     p = Path(path)
#     for p in p.iterdir():
#         print(type(p))
#
# if __name__ == "__main__":
#     if len(argv) == 1:
#         print("Not args")
#     if len(argv)  == 2:
#         read_folder(argv[1])

#
# import re
#
# text = "What is Lorem Ipsum? \
# Lorem Ipsum is simply dummy text of the printing and typesetting industry.\
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, \
# when an unknown printer took a galley of type and scrambled it to make a type \
# specimen book. It has survived not only five centuries, but also the leeap into \
# electronic typesetting, remaining essentially unchanged.\
# It was popularised in the 1960s with the release of Letraset sheets containing\
# Lorem Ipsum passages, and more recently with desktop publishing software like\
# Aldus PageMaker including versions of Lorem Ipsum."
#
# def find_word(word: str, text: str) -> dict:
#     result = re.search(word, text)
#
#     return result # result.span()
#
#
# result = find_word("typesetting", text)
# print(result)

# def find_word(word: str, text: str) -> dict:
#     result = re.search(word, text)
#     result_dict = {"find": False, "start_position": None}
#
#     if result:
#         result_dict["find"] = True
#         result_dict["start_position"] = result.start()
#
#     return result_dict
#
#
# result = find_word("typesetting", text)  # find_word("Python", text)
# print(result)

#
# new_dict = {str(item): item for item in range(10)}
#
# for i in new_dict.values():
#    print(type(i))
#
# def find_key(key: str) -> str | None:
#     result = new_dict.get(key)
#
#     if result:
#         return "Yes"
#
#     return None
#
#
# print(find_key("8"))

#
# new_dict = {str(item): item // 2 for item in range(10)}
# print(new_dict)
#
# def find_same_val(val: int) -> list:
#     result = []
#
#     for k, v in new_dict.items():
#         if v == val:
#             result.append(k)
#
#     return result
#
#
# res = find_same_val(3)
# print(res)

