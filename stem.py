class Stem:
    def __init__(self, color="green"):
        self._color = color

    def draw(self, t, x1, y1, x2, y2):
        t.penup()
        t.goto(x1, y1)
        t.pendown()

        t.color(self._color)
        t.goto(x2, y2)
