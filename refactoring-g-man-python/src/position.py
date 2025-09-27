class Position:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def distance_to(self, to):
        return abs(self._x - to.x) + abs(self._y - to.y)
