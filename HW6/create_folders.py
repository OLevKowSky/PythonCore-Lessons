import json
import sys
from pathlib import Path

path = Path(sys.argv[1])

def create_folders(path: Path) -> str:
    with open(path) as f:
        result = json.load(f)
    return result

CATEGORIES = create_folders("dict.json")

for i in CATEGORIES:
    if not path.joinpath(i).exists():
        path.joinpath(i).mkdir()

if __name__ == "__main__":
    create_folders(path)