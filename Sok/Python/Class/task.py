import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):

        return f"Vector2D({self.x}, {self.y})"

    def __str__(self):

        return f"({self.x}, {self.y})"

    def length(self):

        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle(self):
        angle_rad = math.atan2(self.y, self.x)
        angle_deg = math.degrees(angle_rad)

        if angle_deg < 0:
            angle_deg += 360

        return angle_deg

    def add(self, other_vector):
        new_x = self.x + other_vector.x
        new_y = self.y + other_vector.y

        return Vector2D(new_x, new_y)

    def subtract(self, other_vector):
        new_x = self.x - other_vector.x
        new_y = self.y - other_vector.y

        return Vector2D(new_x, new_y)

    def dot_product(self, other_vector):

        return self.x * other_vector.x + self.y * other_vector.y


v1 = Vector2D(3, 4)
v2 = Vector2D(-1, 5)

print(f"Vector v1: {v1}")
print(f"Vector v2: {v2}")

print(" ")

print(f"Length v1: {v1.length()}")

print(f"Angle v1 to X: {v1.angle()}°")

print(" ")

v_sum = v1.add(v2)
print(f"Sum v1 + v2: {v_sum}")

v_diff = v1.subtract(v2)
print(f"Diff v1 - v2: {v_diff}")

print(" ")

dot_prod = v1.dot_product(v2)
print(f"Skalar proizved: {dot_prod}")