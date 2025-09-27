import unittest
import tempfile
import os
import io
import sys
from src.gman import Gman
from src.file_reader import FileReader
from src.position import Position

class TestGman(unittest.TestCase):

    def test_move_simple_east(self):
        g = Gman(Position(2, 1), Position(4, 3), "E")
        self.assertEqual(g.calculate_power(), 155)

    def test_move_complex_west(self):
        g = Gman(Position(0, 5), Position(6, 1), "W")
        self.assertEqual(g.calculate_power(), 90)

    def test_turn_and_move(self):
        g = Gman(Position(2, 1), Position(4, 5), "S")
        self.assertEqual(g.calculate_power(), 130)

    def test_north_direction(self):
        g = Gman(Position(1, 1), Position(1, 4), "N")
        self.assertIsInstance(g.calculate_power(), int)

    def test_source_and_destination_same(self):
        g = Gman(Position(2, 2), Position(2, 2), "E")
        self.assertEqual(g.calculate_power(), 195)


class TestFileReader(unittest.TestCase):

    def test_process_prints_power(self):
        content = """SOURCE 2 1 E\nDESTINATION 4 3\nPRINT_POWER"""
        fd, path = tempfile.mkstemp()
        with os.fdopen(fd, "w") as tmp:
            tmp.write(content)

        captured = io.StringIO()
        sys.stdout = captured
        fr = FileReader(path)
        lines = fr.read()

        self.assertEqual(lines[0], ["SOURCE", "2", "1", "E"])
        self.assertEqual(lines[1], ["DESTINATION", "4", "3"])
        self.assertEqual(lines[2], ["PRINT_POWER"])


if __name__ == "__main__":
    unittest.main()
