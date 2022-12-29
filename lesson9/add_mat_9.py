## CARRING

# def greeting(mode, name):
#     if mode == "m":
#         print(f"Mr. {name}")
#     elif mode == "f":
#         print(f"Mrs. {name}")
#
#
# def main():
#     greeting("m", "Vlad")
#
#
# if __name__ == "__main__":
#     main()


# def greeting(mode):
#     if mode == "m":
#         return hello_male
#     elif mode == "f":
#         return hello_female
#
#
# def hello_male(name):
#     print(f"Mr. {name}")
#
#
# def hello_female(name):
#     print(f"Mrs. {name}")
#
#
# def main():
#     mr = greeting("m")
#     mrs = greeting("f")
#
#     mr("Vlad")
#     mrs("Olena")
#
#
# if __name__ == "__main__":
#     main()


# def hello_male(name):
#     print(f"Mr. {name}")
#
#
# def hello_female(name):
#     print(f"Mrs. {name}")
#
#
# def hello_pan(name):
#     print(f"Пан {name}")
#
# MODES = {
#     "m": hello_male,
#     "f": hello_female,
#     "pan": hello_pan
# }
#
#
# def greeting(mode):
#     return MODES[mode]
#
#
# def main():
#     mr = greeting("m")
#     mrs = greeting("f")
#     pan = greeting("pan")
#
#     mr("Vlad")
#     mrs("Olena")
#     pan("Тарас")
#
#
# if __name__ == "__main__":
#     main()


## CACHE (Замикання)

# def outer(x):
#     def inner(y):
#         print(f"{x} + {y} = {x + y}")
#     return inner
#
#
# def main():
#     adder_two = outer(2)
#     adder_two(8)
#     adder_three = outer(3)
#     adder_three(8)
#
#
# if __name__ == "__main__":
#     main()


# def get_cache():
#     cache = {}
#     def inner(n):
#         print(cache)
#         if n not in cache:
#             cache[n] = sum([i for i in range(1, n+1)])
#             print(f"Hard work: {n}")
#             return cache[n]
#         else:
#             print(f"Easy work: {n}")
#             return cache[n]
#        
#     return inner
#
#
# def main():
#     calc = get_cache()
#     print(calc(5))
#     print(calc(5))
#     print(calc(10))
#     print(calc(10))
#     print(calc(15))
#     print(calc(5))
#
#
# if __name__ == "__main__":
#     main()


# def get_cache(cache=None):
#     if cache is None:
#         cache = {}
#     def inner(n):
#         print(cache)
#         if n not in cache:
#             cache[n] = sum([i for i in range(1, n+1)])
#             print(f"Hard work: {n}")
#             return cache[n]
#         else:
#             print(f"Easy work: {n}")
#             return cache[n]
#     
#     return inner
#
#
# def main():
#     data = {5: 15, 10: 55, 15: 120}
#     calc = get_cache(data)
#     print(calc(5))
#     print(calc(5))
#     print(calc(10))
#     print(calc(10))
#     print(calc(15))
#     print(calc(5))
#
#
# if __name__ == "__main__":
#     main()


## FUNCTIONAL (lambda, map, filter)

# import math
#
# def get_length(d):
#     result = d * math.pi
#     return result
#
#
# get_lambda_length = lambda d: d * math.pi
#
#
# if __name__ == "__main__":
#    length_1 = get_length(10)
#    length_2 = get_lambda_length(10)
#    print(length_1, length_2, sep="\n")


# def get_ost(data):
#     result = []
#     for n in data:
#         ost = n % 2
#         result.append(ost)
#     return result
#
#
# if __name__ == "__main__":
#     data = [1, 2, 3, 4, 5, 6]
#     ost_1 = get_ost(data)
#     print(*ost_1)
#     ost_2 = map(lambda n: n % 2, data)
#     print(*ost_2)
#     print(*map(lambda n: n % 2, data))


# def check_num(data):
#     result = []
#     for n in data:
#         ost = n % 2
#         if ost:
#             result.append(n)
#     return result
#
#
# if __name__ == "__main__":
#     data = [1, 2, 3, 4, 5, 6]
#     check_data = check_num(data)
#     print(*check_data)
#     check_data_filter = filter(lambda x: not x % 2, data)
#     print(*check_data_filter)


## Decorators

# def args_logger(func):
#     def inner(*args):
#         print(f"I am args logger. Args: {args}")
#         result = func(*args)
#         return result
#     return inner
#
#
# def calc(x, y):
#     result = x + y
#     return result
#
#
# logger = args_logger(calc)
#
#
# if __name__ == "__main__":
#     print(logger(7, 9))


from time import time

def args_logger(func):
    def inner(*args):
        if Debug:
            print(f"I am args logger. Args: {args}")
        result = func(*args)
        return result
    return inner


def result_logger(func):
    def inner(*args):
        result = func(*args)
        if Debug:
            print(f"I am result logger. Result: {result}")
            return result
    return inner


def timer(func):
    def inner(*args):
        start = time()
        result = func(*args)
        stop = time()
        if Debug:
            print(f"I am timer. Run time: {stop - start}")
        return result
    return inner


@timer
@result_logger
@args_logger
def calc(x, y):
    result = x + y
    return result


Debug = True


if __name__ == "__main__":
    print(calc(7, 9))
