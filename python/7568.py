n = int(input())
sizes = []

for _ in range(n):
    x, y = map(int, input().split())
    sizes.append((x, y))

for i in range(n):
    temp = sizes[:i] + sizes[i+1:]
    original = sizes[i]
    rank = 0
    for t in temp:
        if t[0] > original[0] and t[1] > original[1]:
            rank += 1
    print(rank + 1, end=" ")
    