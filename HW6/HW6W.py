import json
import shutil
import sys
from pathlib import Path
# from normalize import normalize

path = Path(r"c:\lesson6")


def create_folders(path: Path) -> str:
    with open(path) as f:
        result = json.load(f)
    return result

CATEGORIES = create_folders("dict.json")

for i in CATEGORIES:
    if not path.joinpath(i).exists():
        path.joinpath(i).mkdir()


def read(path: Path) -> list[Path]:
    lst = []
    for element in path.glob("**/*"):
        lst.append(element)
    # print(lst)

    for element in lst:
        if element.suffix in ('.jpeg', '.png', '.jpg', '.svg'):
            shutil.move(element, "images")
        elif element.suffix in ('.avi', '.mp4', '.mov', '.mkv'):
            shutil.move(element, "video")
        elif element.suffix in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', 'pptx'):
            shutil.move(element, "documents")
        elif element.suffix in ('.mp3', '.ogg', '.wav', '.amr'):
            shutil.move(element, "music")
        elif element.suffix in ('.zip', '.gz', '.tar'):
            shutil.move(element, "archives")
        else:
            shutil.move(element, "els")

read(path)


# def sort(lst):
    
        # print(element)

# sort(lst)


# def create_folders(path: Path) -> str:
#     with open(path) as f:
#         result = json.load(f)
#     return result

# CATEGORIES = create_folders("dict.json")

# for i in CATEGORIES:
#     if not path.joinpath(i).exists():
#         path.joinpath(i).mkdir()

# def rename_file(name: str) -> str:
#     pass


# def archive(path: Path) -> str:
#     pass


# def delete_folder(path: Path) -> str:
    # for element in lst:
    #     if element.is_dir():
    #         element.stat().st_size == 0:
    #             element.rmdir()


# def sort(lst: list[Path]) -> str:
#     for element in lst:
#         if element.is_dir():
#             if file.stat().st_size == 0:
#                 file.rmdir()
#         for suffix in CATEGORIES:
#             if element.suffix in CATEGORIES[suffix]:
#                 dir_img = path / suffix
#                 dir_img.mkdir(exist_ok=True)
#                 element.rename(dir_img.joinpath(element.name))
    

#     if __name__ == "__main__":
#         sort(lst)


# def task() -> str:
#     sort(Path(sys.argv[1]))


# if __name__ == "__main__":
#     task()


#
# import sys
# from pathlib import Path
# from sort import sort
# from suffix import suffix

# try:
#     path = Path(sys.argv[1])

#     def task():

#         if path.exists():
#             suffix()
#             sort()
#         else:
#             print(f"{path.absolute()} is not exist.")   
    

#     if __name__ == "__main__":
#         task()

# except IndexError:
#     print("Path not found. Please, enter path.")
    