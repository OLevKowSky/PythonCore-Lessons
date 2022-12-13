import json
import sys
import shutil
from pathlib import Path

path = Path(r"c:\folder")

def read(path: Path) -> list[Path]:
    lst = []
    for element in path.glob("**/*"):
        # if element.is_file():
        lst.append(element)

    return lst # type = <class 'list'>

read(path)


def create_folders(path):
    with open(path) as f:
        result = json.load(f)
    return result

CATEGORIES = create_folders("dict.json")

# for cat in CATEGORIES.values():
#     print(type(cat)) # type = <class 'list'>

for cat in CATEGORIES:
    if not path.joinpath(cat).exists():
        path.joinpath(cat).mkdir()

folders = []
for cat in CATEGORIES:
    folders.append(cat) # type <class 'list'>

    
    # target = path.joinpath(cat)
    # print(target)
    # print(type(target))


def sort(lst):

    for element in lst:
        if element.is_file():
            for cat, suff in CATEGORIES.items():
                if element.suffix in suff:
                    try:
                        element.rename(path.joinpath(cat).joinpath(element.name))
                    except FileExistsError:
                        element.unlink()
      

sort(read(path))


def delete_folder(lst):
    for element in lst:
        if element.is_dir():
            if element.stat().st_size == 0:
                if not element.name in folders:
                    element.rmdir()


delete_folder(read(path))
    