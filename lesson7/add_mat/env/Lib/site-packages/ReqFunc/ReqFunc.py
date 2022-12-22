import json
import shutil
import sys
from pathlib import Path
from normalize import normalize

path = Path(sys.argv[1])


def create_folders(path):

    with open(path) as f:
        result = json.load(f)

    return result

CATEGORIES = create_folders("dict.json")

for cat in CATEGORIES:
    if not path.joinpath(cat).exists():
        path.joinpath(cat).mkdir()

folders = []

for cat in CATEGORIES:
    folders.append(cat)


def rename(path):
    
    for element in path.glob("**/*"):
        name = element.name
        new_element = normalize(name)

        try:
            element.rename(path.joinpath(path).joinpath(new_element))
        except FileExistsError:
            pass


if __name__ == "__main__":
    rename(path)


def read(path: Path) -> list[Path]:

    lst = []

    for element in path.glob("**/*"):
        lst.append(element)
        
    return lst


if __name__ == "__main__":
    read(path)


def sort(lst):

    for element in lst:
        if element.is_file():
            for cat, suff in CATEGORIES.items():
                if element.suffix in suff:
                    try:
                        element.rename(path.joinpath(cat).joinpath(element.name))
                    except FileExistsError:
                        name = element.stem
                        new_name = str(name) + ("_copy") + element.suffix
                        element.rename(path.joinpath(cat).joinpath(new_name))
                # else:
                #     try:
                #         element.rename(path.joinpath("else").joinpath(element.name))
                #     except FileExistsError:
                #         name = element.stem
                #         new_name = str(name) + ("_copy") + element.suffix
                #         element.rename(path.joinpath("else").joinpath(new_name))
      

if __name__ == "__main__":
    sort(read(path))


def delete_folder(path):

    for element in path.iterdir():
        if element.is_dir():
            if not element.name in folders:
                shutil.rmtree(element)


if __name__ == "__main__":
    delete_folder(path)


def unpack(path):

    extract_dir = path.joinpath("archives")

    for archive in extract_dir.iterdir():
        shutil.unpack_archive(archive, extract_dir.joinpath(archive.stem))
        archive.unlink()


if __name__ == "__main__":
    unpack(path)


def suffix(path):

    kn_suffix = []
    unkn_suffix = []

    if path.is_dir():
        elements = path.glob("**/*")
        for element in elements:
            if element.suffix in ('.jpeg', '.png', '.jpg', '.svg'):
                kn_suffix.append(element.suffix)
            elif element.suffix in ('.avi', '.mp4', '.mov', '.mkv'):
                kn_suffix.append(element.suffix)
            elif element.suffix in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', 'pptx'):
                kn_suffix.append(element.suffix)
            elif element.suffix in ('.mp3', '.ogg', '.wav', '.amr'):
                kn_suffix.append(element.suffix)
            elif element.suffix in ('.zip', '.gz', '.tar'):
                kn_suffix.append(element.suffix)
            else:
                unkn_suffix.append(element.suffix)

    kn_suffix = set(kn_suffix)
    unkn_suffix = set(unkn_suffix)
    print(f"Known suffix: {kn_suffix}")
    print(f"Unknown suffix: {unkn_suffix}")


if __name__ == "__main__":
    suffix(path)
