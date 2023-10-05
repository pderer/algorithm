n = int(input())
work_list = [] # 1일차 부터 n일차 까지 잡혀 있는 상담 index 0 ~ n - 1
for i in range(n):
    work_list.append(list(map(int, input().split())))

d = [0] * (n + 1) # n일차 받을 수 있는 금액
max_value = 0

for i in range(n - 1, -1, -1):
    time = work_list[i][0] + i
    if time <= n:
        d[i] = max(work_list[i][1] + d[time], max_value)
        max_value = d[i]
    else:
        d[i] = max_value

print(max_value)