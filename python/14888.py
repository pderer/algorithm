from collections import deque
from itertools import permutations


n = int(input())
num_list = list(map(int, input().split()))
operators_list = list(map(int, input().split())) # 0:더하기, 1:빼기, 2:곱셈, 3:나누기

operator_data = []

for i in range(4):
    for j in range(operators_list[i]):
        operator_data.append(i)

oper_perm = list(permutations(operator_data, n - 1))
no_dup_perm = []

for perm in oper_perm:
    if perm in no_dup_perm:
        continue
    else:
        no_dup_perm.append(perm)

# print(no_dup_perm)
maximum = 9999999999
minimum = 9999999999

for perm in no_dup_perm:
    queue = deque()
    queue.append((num_list[0], perm[0], num_list[1], 0)) # 좌항, 연산자, 우항, index
    while queue:
        left, op, right, index = queue.popleft()
        if op == 0:
            temp = left + right
            if index == n - 2:
                if maximum < temp:
                    maximum = temp
                if minimum > temp:
                    minimum = temp
                break
            queue.append((temp, perm[index + 1], num_list[index + 2], index + 1))
        elif op == 1:
            temp = left - right
            if index == n - 2:
                if maximum < temp:
                    maximum = temp
                if minimum > temp:
                    minimum = temp
                break
            queue.append((temp, perm[index + 1], num_list[index + 2], index + 1))
        elif op == 2:
            temp = left * right
            if index == n - 2:
                if maximum < temp:
                    maximum = temp
                if minimum > temp:
                    minimum = temp
                break
            queue.append((temp, perm[index + 1], num_list[index + 2], index + 1))
        elif op == 3:
            temp = 0
            if left < 0 and right > 0:
                temp = (-left) // right
                temp = -(temp)
            else:
                temp = left // right
            if index == n - 2:
                if maximum < temp:
                    maximum = temp
                if minimum > temp:
                    minimum = temp
                break
            queue.append((temp, perm[index + 1], num_list[index + 2], index + 1))

print(maximum)
print(minimum)


