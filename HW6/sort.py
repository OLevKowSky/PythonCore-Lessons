# import json
import shutil
import sys
from pathlib import Path

path = Path(sys.argv[1])

def sort():

    Path.mkdir("images")
    Path.mkdir("video")
    Path.mkdir("documents")
    Path.mkdir("music")
    Path.mkdir("archives")
    Path.mkdir("els")
    
    if path.is_dir():
        elements = path.glob("**/*")
        for element in elements:
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
    

    # print(f"Images: {images}")
    # print(f"Video files: {video}")
    # print(f"Documents: {documents}")
    # print(f"Music files: {music}")
    # print(f"Archives: {archives}")
    # print(f"Unknown files: {els}")


    if __name__ == "__main__":
        sort()




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