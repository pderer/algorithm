import sys

input = sys.stdin.readline

n = int(input().rstrip())

lines = []
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    lines.append((a, 1))
    lines.append((b, -1))

lines.sort()

total = 0
count = 0

for _, point in lines:
    count += point
    total = max(total, count)

print(total)