import json
import sys
from pathlib import Path
from normalize import normalize

path = Path(r"c:\folder")


def read(path: Path) -> list[Path]:
    lst = []
    for element in path.glob("**/*"):
        lst.append(element)
    
    return lst


read(path)


# def create_target_folders(path: Path) -> str: # str, що все створено вдало
#     pass


# def rename_file(name: str) -> str:
#     pass


# def archive(path: Path) -> str: str, що все розархівовано вдало
#     pass


# def delete_folder(path: Path) -> str:
#     for element in lst:
#         if element.is_dir():
#             if element.stat().st_size == 0:
#                 element.rmdir()


def sort_files(path: Path) -> str: # (lst: list[Pass]) з def read
    path.rename(rename_file(path.name))

    pass


# def task() -> str: # розташовувати функції в порядку їх виклику, або ланцюгово або в середині
#     print(sort_files(Path(r"c:\folder")))


# if __name__ == "__main__":
#     task()