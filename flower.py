import turtle
from petal import Petal
from leaf import Leaf
from stem import Stem

class Flower:
    def __init__(self, petals_count, petal_color, stem_length, leaf_size):
        self._petals = [Petal(color=petal_color) for _ in range(petals_count)]
        self._leaf = Leaf(size=leaf_size)
        self._stem = Stem(length=stem_length)
    def draw(self):
        t = turtle.Turtle()
        t.speed(0)
        self._stem.draw(t)

        t.backward(50)
        t.left(45)
        self._leaf.draw(t)
        t.right(45)

        t.setheading(0)
        t.color("yellow")
        t.begin_fill()
        t.circle(20)
        t.end_fill()

        for petal in self._petals:
            t.penup()
            t.goto(0, 0)
            t.forward(40)
            t.pendown()
            petal.draw(t)
            t.penup()
            t.goto(0, 0)
            t.right(360 / len(self._petals))

        turtle.done()
