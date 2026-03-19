class Leaf:
    def __init__(self, color="green", size=15):
        self._color = color
        self._size = size

    def draw(self, t, x, y):
        t.penup()
        t.goto(x, y)
        t.setheading(45)
        t.pendown()

        t.color(self._color)
        t.begin_fill()
        t.circle(self._size, 60)
        t.left(120)
        t.circle(self._size, 60)
        t.end_fill()
