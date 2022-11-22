import name_main2
from name_main2 import f4 as function4

print(f" name_main1 __name__ is set to:{__name__}")

def f1():
    print("Function 1")


def f2():
    print("Function 2")


if __name__ == "__main__":
    print("name_main1 executed when run directly")
    f2()
    name_main2.f3()
    function4()
else:
    print("name_main1 executed when imported")
