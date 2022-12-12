import sys
from pathlib import Path
from sort import sort
from suffix import suffix

try:
    path = Path(sys.argv[1])

    def task():

        if path.exists():
            suffix()
            sort()
        else:
            print(f"{path.absolute()} is not exist.")   
    

    if __name__ == "__main__":
        task()

except IndexError:
    print("Path not found. Please, enter path.")



# def task() -> str: # розташовувати функції в порядку їх виклику, або ланцюгово або в середині
#     print(sort(Path(r"c:\folder"))) # Path(sys.argv[1])


# if __name__ == "__main__":
#     task()
