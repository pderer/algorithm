n = int(input())
rest_list = list(map(int, input().split()))
customer_limit = list(map(int, input().split()))
count = 0

for i in range(len(rest_list)):
    rest_list[i] -= customer_limit[0] # 팀장 한명이 맡을 수 있는 사람 빼기
    count += 1

for i in range(len(rest_list)):
    if rest_list[i] <= 0:
        continue
    div, mod = divmod(rest_list[i], customer_limit[1])
    if div == 0:
        count += 1
    if div > 0 and mod == 0:
        count += div
    elif div > 0 and mod != 0:
        count += (div + 1)
print(count)