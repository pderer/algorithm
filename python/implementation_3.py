point = input()
x, y = 0, 0
y = int(point[1])
count = 0

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

if point[0] == "a":
    x = 1
elif point[0] == "b":
    x = 2
elif point[0] == "c":
    x = 3
elif point[0] == "d":
    x = 4
elif point[0] == "e":
    x = 5
elif point[0] == "f":
    x = 6
elif point[0] == "g":
    x = 7
elif point[0] == "h":
    x = 8

for i in range(8):
    temp_x = x + dx[i]
    temp_y = y + dy[i]
    if temp_x < 1 or temp_y < 1 or temp_x > 8 or temp_y > 8:
        continue
    count += 1

print(count)