class Stem:
    def __init__(self, length=100, color="green"):
        self._length = length
        self._color = color

    def draw(self, t):
        t.color(self._color)
        t.setheading(-90)
        t.forward(self._length)
