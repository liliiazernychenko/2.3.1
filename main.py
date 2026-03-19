import turtle
from flower import Flower
def read_config(filename):
    config = {}
    with open(filename, "r") as f:
        for line in f:
            key, value = line.strip().split("=")
            config[key] = value
    return config

if __name__ == "__main__":
    filename = input("Введіть шлях файлу (наприклад: tests/test1.txt): ")
    config = read_config(filename)
    t = turtle.Turtle()
    t.speed(0)
    base_x, base_y = 0, -150
    flowers_positions = [
        (0, 0),
        (-40, 50),
        (40, 50),
        (-20, 100),
        (20, 100)
    ]

    colors = ["red", "blue", "purple", "pink", "orange"]
    for i, (x, y) in enumerate(flowers_positions):
        flower = Flower(
            petals_count=int(config["petals"]),
            petal_color=config["petal_color"]
        )
        flower.draw(t, base_x, base_y, x, y)

    turtle.done()
    with open("output.txt", "w") as f:
        f.write("Bouquet drawn successfully\n")
        f.write(f"Flowers count: {len(flowers_positions)}\n")
