from sys import argv

from src.extractor import Extractor
from src.file_reader import FileReader


def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    file = FileReader(file_path)
    file_content = file.read()
    extractor = Extractor()
    extractor.process(file_content)


if __name__ == "__main__":
    main()
