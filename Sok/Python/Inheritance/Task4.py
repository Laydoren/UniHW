import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def volume(self):
        return 0

    def __str__(self):
        return f"{self.name}: Площадь = {self.area()}, Объем = {self.volume()}"

class Cube(Shape):
    def __init__(self, side):
        super().__init__("Куб")
        self.side = side

    def area(self):
        return 6 * (self.side ** 2)

    def volume(self):
        return self.side ** 3

class Sphere(Shape):
    def __init__(self, radius):
        super().__init__("Сфера")
        self.radius = radius

    def area(self):
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

class Cylinder(Shape):
    def __init__(self, radius, height):
        super().__init__("Цилиндр")
        self.radius = radius
        self.height = height

    def area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

class Parallelepiped(Shape):
    def __init__(self, a, b, c):
        super().__init__("Параллелепипед")
        self.a, self.b, self.c = a, b, c

    def area(self):
        return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)

    def volume(self):
        return self.a * self.b * self.c

class Ellipsoid(Shape):
    def __init__(self, a, b, c):
        super().__init__("Эллипсоид")
        self.a, self.b, self.c = a, b, c

    def area(self):
        p = 1.6075
        return 4 * math.pi * (((self.a**p * self.b**p + self.a**p * self.c**p + self.b**p * self.c**p) / 3) ** (1/p))

    def volume(self):
        return (4/3) * math.pi * self.a * self.b * self.c


def check_volumes(shapes):
    total_volume = sum(s.volume() for s in shapes)
    found = False

    for shape in shapes:
        current_vol = shape.volume()
        others_vol = total_volume - current_vol

        if current_vol >= others_vol:
            print(f"Найдена фигура: {shape}")
            print(f"Ее объем ({current_vol}) >= суммы остальных ({others_vol})")
            found = True

    if not found:
        print("Нет доминирующих по объёму фигур")

Cubik = Cube(89)
print(Cubik.__str__())

print()

lst = [Cube(3), Sphere(3),Cylinder(2, 5),Parallelepiped(2, 3, 4),Ellipsoid(2, 1.5, 1)]
lst2 = [Cube(3), Sphere(39),Cylinder(2, 5),Parallelepiped(2, 3, 4),Ellipsoid(2, 1.5, 1)]

check_volumes(lst)

print()

check_volumes(lst2)