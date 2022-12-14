import json
import sys
import shutil
from pathlib import Path
from normalize import normalize

path = Path(r"c:\folder")

def read(path: Path) -> list[Path]:
    lst = []
    for element in path.glob("**/*"):

        name = element.name
        new_element = normalize(name)

        try:
            element.rename(path.joinpath(path).joinpath(new_element))
        except FileExistsError:
            pass

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
                # else:
                #     try:
                #         element.rename(path.joinpath("else").joinpath(element.name))
                #     except FileExistsError:
                #         element.unlink()
      

sort(read(path))


def delete_folder(path):

    for element in path.iterdir():
        if element.is_dir():
            if not element.name in folders:
                shutil.rmtree(element)


delete_folder(path)


def unpack(path):

    extract_dir = path.joinpath("archives")

    for archive in extract_dir.iterdir():
        shutil.unpack_archive(archive, extract_dir.joinpath(archive.stem))
        archive.unlink()


unpack(path)
