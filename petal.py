class Petal:
    def __init__(self, color="red", radius=50):
        self._color = color
        self._radius = radius

    def draw(self, t):
        t.color(self._color)
        t.begin_fill()
        t.circle(self._radius)
        t.end_fill()
