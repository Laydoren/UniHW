n = int(input())
town_roads = [list(map(int, input().split())) for i in range(n)]

roads = 0
for i in range(n):
    for j in range(n):
        if town_roads[i][j] == 1 and j > i:
            roads += 1

print(roads)