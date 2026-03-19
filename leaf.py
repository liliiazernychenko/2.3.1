class Leaf:
    def __init__(self, color="green", size=40):
        self._color = color
        self._size = size

    def draw(self, t):
        t.color(self._color)
        t.begin_fill()
        t.circle(self._size, 60)
        t.left(120)
        t.circle(self._size, 60)
        t.end_fill()
