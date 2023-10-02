n = int(input())

plan_list = list(input().split())

start = [1, 1]

for plan in plan_list:
    if plan == "R":
        if start[1] < n:
            start[1] += 1
    elif plan == "L":
        if start[1] > 1:
            start[1] -= 1
    elif plan == "U":
        if start[0] > 1:
            start[0] -= 1
    elif plan == "D":
        if start[0] < n:
            start[0] += 1

print(start[0], start[1])