import json
import sys
from pathlib import Path

path = Path(r"c:\folder")

def read(path: Path) -> list[Path]:
    lst = []
    for element in path.glob("**/*"):
        if element.is_file():
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

for i in CATEGORIES:
    if not path.joinpath(i).exists():
        path.joinpath(i).mkdir()

    # print(type(path.joinpath(i)))


def sort(lst):

    for element in lst:
        # print(element) # type = <class 'pathlib.WindowsPath'>
        for cat, suff in CATEGORIES.items():
            if element.suffix in suff:
                print(cat)
                # path.joinpath(i).joinpath(element)
#             # elif element.suffix in ('.avi', '.mp4', '.mov', '.mkv'):
#             #     shutil.move(element, "video")
#             # elif element.suffix in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', 'pptx'):
#             #     shutil.move(element, "documents")
#             # elif element.suffix in ('.mp3', '.ogg', '.wav', '.amr'):
#             #     shutil.move(element, "music")
#             # elif element.suffix in ('.zip', '.gz', '.tar'):
#             #     shutil.move(element, "archives")
#             # else:
#             #     element.rename(Path("else").joinpath(element.name))

sort(read(path))


# def sort(lst):
    
        # print(element)

# sort(lst)
    