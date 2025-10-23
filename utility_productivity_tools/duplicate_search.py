import hashlib
import sys
from collections import defaultdict
from pathlib import Path

def get_checksum(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()

def get_duplicates(directory: Path) -> dict[str, list[Path]]:
    files: defaultdict[str, list[Path]] = defaultdict(list)
    for child in directory.iterdir():
        if child.is_dir():
            files.update(get_duplicates(child))
        else:
            files[get_checksum(child.read_bytes())].append(child)
    return files

def main():
    try:
        directory = sys.argv[1]
    except IndexError:
        directory = "."
    duplicates = get_duplicates(Path(directory))
    for paths in duplicates.values():
        if len(paths) == 1:
            continue
        for n, path in enumerate(path):
            print(f"{n}. {path}")
        try:
            delete = map(int, input("Delete? (e.b. 0, 1, 3) ")).split(",")
            for num in delete:
                paths[sum].unlink()
        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    main()