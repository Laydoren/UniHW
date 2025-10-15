row, column = map(int, input().split())
table = [[i*j for j in range(1, column + 1)] for i in range(1, row + 1)]

red = green = blue = black = 0

for row in table:
    for num in row:
        if num % 5 == 0:
            blue += 1
        elif num % 3 == 0:
            green += 1
        elif num % 2 == 0:
            red += 1
        else:
            black += 1

print(f"RED : {red}")
print(f"GREEN : {green}")
print(f"BLUE : {blue}")
print(f"BLACK : {black}")