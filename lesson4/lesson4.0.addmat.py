"""lists"""

# text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# words = text.split() # 1й спосіб
# print(words)

# words = [] # 2й спосіб
# start = 0
# for indx, char in enumerate(text):
#     if not char.lower() in alphabet:
#         word = text[start:indx]
#         words.append(word.strip())
#         start = indx
#
# print(words)


"""dicts"""

# text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

# dict_counter = {} # {'L':1, 'o':2} # 1й спосіб
# for char in text:
#     try:
#         count = dict_counter[char] # отримаємо значення по ключу
#     except KeyError:
#         count = 0
#     count += 1
#     dict_counter[char] = count # записуємо значення по ключу
#
# print(dict_counter)

# dict_counter = {}  # {'L':1, 'o':2} # 2й спосіб
# for char in text:
#     count = dict_counter.get(char, 0)
#     count += 1
#     dict_counter[char] = count  # записуємо значення по ключу
#
# print(dict_counter)


"""set"""

text = "What is Lorem Ipsum? \
Lorem Ipsum is simply dummy text of the printing and typesetting industry.\
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, \
when an unknown printer took a galley of type and scrambled it to make a type \
specimen book. It has survived not only five centuries, but also the leeap into \
electronic typesetting, remaining essentially unchanged.\
It was popularised in the 1960s with the release of Letraset sheets containing\
Lorem Ipsum passages, and more recently with desktop publishing software like\
Aldus PageMaker including versions of Lorem Ipsum."

alphabet = "abcdefghijklmnopqrstuvwxyz"

char_set = set()
symbol_set = set()

for el in text:
    if el.lower() in alphabet:
        char_set.add(el)
    else:
        symbol_set.add(el)

print(f"Chars {char_set}")
print(f"Symbols {symbol_set}")
