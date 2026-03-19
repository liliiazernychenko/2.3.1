class Petal:
    def __init__(self, color="red", radius=20):
        self._color = color
        self._radius = radius

    def draw(self, t, cx, cy, angle):
        t.penup()
        t.goto(cx, cy)
        t.setheading(angle)
        t.forward(30)
        t.pendown()

        t.color(self._color)
        t.begin_fill()
        t.circle(self._radius)
        t.end_fill()
