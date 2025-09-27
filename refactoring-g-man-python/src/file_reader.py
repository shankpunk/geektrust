class FileReader:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        with open(self.filepath) as f:
            return [line.strip().split() for line in f]
