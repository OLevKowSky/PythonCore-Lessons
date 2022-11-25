# from pathlib import Path  # для папки "test0" в терміналі вводимо "python .\lesson4.0.py test0"
# der sort_format(folder):
#     for file in folder:
#         if

from pathlib import Path
import sys

p = Path(sys.argv[1])


def parse_folder_recursion(path):

    # images = []
    # video = []
    # documents = []

    for element in path.iterdir():
        if element.is_dir():
            print(f"This is folder {element.name}")
            parse_folder_recursion(element)
        else:
            # print(f"This is file {element.name}")
            print(element.suffixes)  # ['.tar', '.gz ']


if __name__ == "__main__":
    parse_folder_recursion(p)

# зображення('JPEG', 'PNG', 'JPG', 'SVG')
# відео файли('AVI', 'MP4', 'MOV', 'MKV')
# документи('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
# музика('MP3', 'OGG', 'WAV', 'AMR')
# архіви('ZIP', 'GZ', 'TAR')
# невідомі розширення.
