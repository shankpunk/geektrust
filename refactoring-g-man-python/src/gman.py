from src.direction import Direction
from src.constants import BASE_POWER, DISTANCE_COST, TURN_COST


class Gman:

    def __init__(self, source, destination, direction):
        self.source = source
        self.destination = destination
        self.direction = Direction[direction].value

    def calculate_power(self):
        dir_xy = self.direction

        move_x = self.destination.x - self.source.x
        move_y = self.destination.y - self.source.y
        move_dir = (move_x // abs(move_x) if move_x != 0 else 0, move_y // abs(move_y) if move_y != 0 else 0)

        distance = self.source.distance_to(self.destination)
        turns = max(abs(move_dir[0] - dir_xy[0]), abs(move_dir[1] - dir_xy[1]))
        r = BASE_POWER - ((distance * DISTANCE_COST) + (turns * TURN_COST))
        return r
