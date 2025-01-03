class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point is {self.x} {self.y}")


point = Point(1, 2)

print(point.default_color)
