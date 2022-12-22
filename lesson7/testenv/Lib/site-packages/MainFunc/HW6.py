import sys
from pathlib import Path
from ReqFunc.ReqFunc import *

try:
    path = Path(sys.argv[1])

    def task():

        if path.exists():          

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


            rename(path)
            read(path)
            sort(read(path))
            delete_folder(path)
            unpack(path)
            suffix(path)

        else:
            print(f"{path.absolute()} is not exist.")   
    

    if __name__ == "__main__":
        task()

except IndexError:
    print("Path not found. Please, enter path.")
