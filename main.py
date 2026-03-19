from flower import Flower
def read_config(filename):
    config = {}
    with open(filename, "r") as f:
        for line in f:
            key, value = line.strip().split("=")
            config[key] = value
    return config
if __name__ == "__main__":
    config = read_config("tests/test1.txt")

    flower = Flower(
        petals_count=int(config["petals"]),
        petal_color=config["petal_color"],
        stem_length=int(config["stem_length"]),
        leaf_size=int(config["leaf_size"])
    )

    flower.draw()
    with open("output.txt", "w") as f:
        f.write("Program executed successfully\n")
        f.write(f"Petals: {config['petals']}\n")
        f.write(f"Color: {config['petal_color']}\n")
