

print(f" name-main2 __name__ is set to:{__name__}")



def f3():
    print("Function 3")


def f4():
    print("Function 4")


if __name__ == "__main__":
    print("name_main1 executed when ran directly")
else:
    print("name_main1 executed when imported")
