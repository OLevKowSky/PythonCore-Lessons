"""Lesson4.1.
   Collection"""

# LISTS

# l = ["foo", "bar", 1, 2, [4, 5]]

# print("LIST L ", l)
# print("Type L ", type(l))

# l2 = ["alisa", "bob"]

# print("Is l equal l2 ", l == l2)

# SLICES

# print(l[2])
# print(l[-1])

# print(l[2:5])
# print(l[-4:-2])

# print(l[2:], l[0:4])

# START : END: STEP

# print(l[0:4:2])
# print(l[0::2])
# print(l[::-1])

# print("foo" in l)
# print("pass" in l)

# print(l + l2)
# print(l*3)
# print("Length of list l ", len(l))

# print(l[4][0])

# l[1] = "name"
# print(l)

# l.append("hello")
# print(l)

# l.extend([6, 7, 8])
# print(l)

# l.clear()
# print(l)

# l.insert(2, "pass")
# print(l)

# l.remove("foo")
# print(l)

# l.pop(-3)
# print(l)

# l.reverse()
# print(l)

# TUPLE

# t = ()
# print(type(t))

# t = ("foo", "bar", "baz", "pass")

# print(t[0])
# print(t[1:3])
# print(t[::-1])

# РОЗПАКУВАННЯ

# (v1, v2, v3, v4) = t
# print(type(v1))

# DICTIONARIES

# how to create:

# d1 = {
#     "name": "alisa",
#     "age": 22,
# }
#
# d2 = dict(name="bob", age=25)

# print("D1", d1)
# print("D2", d2)

# print(d1["name"])

# how to add:

# d1["location"] = "London"
# print("D1", d1)

# d1.update({"job": "test"})
# print("D1", d1)

# print(len(d1.))
# print(len(d1.values()))

# d1.clear()
# print("D1", d1)

# print("D1", d1.get("abc", None))

# print("ITEMS ", d1.items())
# print("ITEMS ", list(d1.items()))

# print(d1.keys())
# print(d1.values())

# print("D1 ", d1)
# d1.popitem()
# print("D1 ", d1)


# SET

# s = set(["foo", "bar", "baz"])
# print("SET ", s)

# s = {1, 2, 3, 4,}
# s.add(5)

# print("SET ", s)

# new_s = set([1, 2, [3, 4]])
#
# print("NEW SET ", new_s)

# s = set(["foo", "bar", "baz"])
#
# s_str = set("foo")
# print("SET STR ", s_str)

s2 = {4, "foo", None, True, (2, 3)}
print("SET ", s2)
