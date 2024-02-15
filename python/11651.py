n = int(input())
positions = []

for _ in range(n):
    positions.append(tuple(map(int, input().split())))

positions.sort(key=lambda x: (x[1], x[0]))

for pos in positions:
    print(pos[0], pos[1])