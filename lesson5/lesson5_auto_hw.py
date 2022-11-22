# 1
# import re
# 
# def real_len(text):
#     pattern = r'[^\n, \f, \r, \t, \v]'
#     p = re.findall(pattern, text)
#     return len(p)
# 
# 
# print(real_len("Alex\nKdfe23\t\f\v.\r"))

# 2
# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]
# 
# 
# def find_articles(key, letter_case=False):
#     find_dict = []
#     for article in articles_dict:
#         for k, v in article.items():
#             if letter_case:
#                 a = str(v).find(key)
#                 if a >= 0:
#                     find_dict.append(article)
#             else:
#                 v2 = str(v).lower()
#                 key2 = key.lower()
#                 a = str(v2).find(key2)
#                 if a >= 0:
#                     find_dict.append(article)
#     return find_dict
# 
# 
# print(find_articles("Endless ocean waters."))

# 3
# import re
# 
# def sanitize_phone_number(phone):
#     ph1 = phone.replace("(", "")
#     ph2 = ph1.replace(")", "")
#     ph3 = ph2.replace("+", "")
#     ph4 = ph3.replace("-", "")
#     clean_phone = ph4.replace(" ", "")
#     return clean_phone
# 
# print(sanitize_phone_number("    +38(050)123-32-34"))

# 4

