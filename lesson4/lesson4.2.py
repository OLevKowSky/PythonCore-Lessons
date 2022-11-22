"""lesson 4.2.
   Practice"""

# x1 = {"boor", "baz", "foo"}
# x2 = {"alisa", "xx", "baz"}
# x3 = frozenset(["bob", "mike", "leo"])
# print("Type x3 ", type(x3))
# print(x3.add("pizza")) #Error

# x = x1 | x2
# print(x)

# print(x1.union(x2))

# x = x1 & x2
# print(x)

# print(x1.intersection(x2))

# print(x1.difference(x2))
# print(x2.difference(x1))

# x = x1 ^ x2
# print(x)


# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# expected = ["My", "name", "is", "Kelly"] # очікуваний результат

# list3 = [l1 + l2 for l1, l2 in zip(list1, list2)]
# print("l3 ", list3)

# for i in range(len(list1)): # переносить слова з нового рядка
#     list1[i] = list1[i] + list2[i]
#     print(list1[i])


# numbers = [1, 2, 3, 4, 5]
# expected = [1, 4, 9, 16, 25]  #очікуваний результат

# res = []
# for n in numbers:
#     res.append(n ** 2)
# print(res)

# res = [n ** 2 for n in numbers]
# print(res)


# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# 10 400 #очікуваний результат
# 20 300
# 30 200
# 40 100

# for l1, l2 in zip(list1, list2[::-1]):
#     print(l1, l2)


# list1 = ["Mike", "Alisa", "", "Bob", ""]
# res = list(filter(None, list1))
# print("RES ", res)


# employee_dict = {
#     "dev": {"name": "Alisa", "salary": 1000},
#     "qa": {"name": "Bob", "salary": 1200}
# }
#
# employee_dict["dev"]["salary"] = 1200
#
# print("EMP ", employee_dict)


# dict1 = {
#     "Alisa": 1200,
#     "Bob": 1000,
#     "Mike": 500
# }
#
# print(min(dict1, key=dict1.get))


# emp_location = {
#     "name": "Alisa",
#     "age": 24,
#     "salary": 1200,
#     "city": "New York"
# }
#
# emp_location["location"] = emp_location.pop("city")
# print("EMP LOCATION ", emp_location)


# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# expected = set1 ^ set2 # унікальні в обох списках
# print(expected)

# set1.intersection_update(set2) # однакові в обох
# print(set1)

t1 = (1, 2)
t2 = (3, 4)

t1, t2 = t2, t1

print(t1)
print(t2)

