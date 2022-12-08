import sys
from pathlib import Path

path = Path(sys.argv[1])

def suffix():

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
        suffix()
