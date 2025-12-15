class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            new_proteins = self.proteins + other.proteins
            new_fats = self.fats + other.fats
            new_carbohydrates = self.carbohydrates + other.carbohydrates
            return FoodInfo(new_proteins, new_fats, new_carbohydrates)
        else:
            return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            new_proteins = self.proteins * n
            new_fats = self.fats * n
            new_carbohydrates = self.carbohydrates * n
            return FoodInfo(new_proteins, new_fats, new_carbohydrates)
        else:
            return NotImplemented

    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            new_proteins = self.proteins / n
            new_fats = self.fats / n
            new_carbohydrates = self.carbohydrates / n
            return FoodInfo(new_proteins, new_fats, new_carbohydrates)
        else:
            return NotImplemented

    def __floordiv__(self, n):
        if isinstance(n, (int, float)):
            new_proteins = self.proteins // n
            new_fats = self.fats // n
            new_carbohydrates = self.carbohydrates // n
            return FoodInfo(new_proteins, new_fats, new_carbohydrates)
        else:
            return NotImplemented


food1 = FoodInfo(10, 5, 30)
food2 = FoodInfo(20.5, 15, 50.1)

print(f"food1: {food1}")
print(f"food2: {food2}")

print("")

food_sum = food1 + food2
print(f"food1 + food2: {food_sum}")

print("")

food_mul_right = food1 * 2
print(f"food1 * 2: {food_mul_right}")

print("")

food_div = food1 / 4
print(f"food1 / 4: {food_div}")

print("")

food_floor_div = food2 // 10
print(f"food2 // 10: {food_floor_div}")
