from src.gman import Gman
from src.position import Position


class Extractor:
    def __init__(self):
        self.source = None
        self.destination = None
        self.direction = None

    def process(self, lines):
        for text in lines:
            command = text[0]
            if command == "SOURCE":
                self.source = Position(int(text[1]), int(text[2]))
                self.direction = text[3]
            elif command == "DESTINATION":
                self.destination = Position(int(text[1]), int(text[2]))
            elif command == "PRINT_POWER":
                gman = Gman(self.source, self.destination, self.direction)
                print(f"POWER {gman.calculate_power()}")
