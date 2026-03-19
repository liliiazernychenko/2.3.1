from petal import Petal
from leaf import Leaf
from stem import Stem

class Flower:
    def __init__(self, petals_count, petal_color):
        self._petals = [Petal(petal_color) for _ in range(petals_count)]
        self._leaf = Leaf()
        self._stem = Stem()

    def draw(self, t, base_x, base_y, x, y):
        self._stem.draw(t, base_x, base_y, x, y)
        mid_x = (base_x + x) / 2
        mid_y = (base_y + y) / 2
        self._leaf.draw(t, mid_x, mid_y)
        radius = 15
        t.penup()
        t.goto(x, y - radius)
        t.pendown()
        t.color("yellow")
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        inner = 6
        t.penup()
        t.goto(x, y - inner)
        t.pendown()
        t.color("orange")
        t.begin_fill()
        t.circle(inner)
        t.end_fill()
        n = len(self._petals)
        for i, petal in enumerate(self._petals):
            angle = 360 / n * i
            petal.draw(t, x, y, angle)
