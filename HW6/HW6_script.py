from pathlib import Path
import sys
import os

try:
    path = Path(sys.argv[1])

    def task():

        if path.exists():
            sort()
        else:
            print(f"{path.absolute()} is not exist.")

    def sort():

        images = []
        video = []
        documents = []
        music = []
        archives = []
        els = []
        kn_suffix = []
        unkn_suffix = []

        if path.is_dir():
            elements = path.glob("**/*")
            for element in elements:
                if element.suffix in ('.jpeg', '.png', '.jpg', '.svg'):
                    images.append(element.name)
                    kn_suffix.append(element.suffix)
                elif element.suffix in ('.avi', '.mp4', '.mov', '.mkv'):
                    video.append(element.name)
                    kn_suffix.append(element.suffix)
                elif element.suffix in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', 'pptx'):
                    documents.append(element.name)
                    kn_suffix.append(element.suffix)
                elif element.suffix in ('.mp3', '.ogg', '.wav', '.amr'):
                    music.append(element.name)
                    kn_suffix.append(element.suffix)
                elif element.suffix in ('.zip', '.gz', '.tar'):
                    archives.append(element.name)
                    kn_suffix.append(element.suffix)
                else:
                    els.append(element.name)
                    unkn_suffix.append(element.suffix)

        kn_suffix = set(kn_suffix)
        unkn_suffix = set(unkn_suffix)
        print(f"Images: {images}")
        print(f"Video files: {video}")
        print(f"Documents: {documents}")
        print(f"Music files: {music}")
        print(f"Archives: {archives}")
        print(f"Unknown files: {els}")
        print(f"Known suffix: {kn_suffix}")
        print(f"Unknown suffix: {unkn_suffix}")

    if __name__ == "__main__":
        task()

except IndexError:
    print("Path not found. Please, enter path.")
