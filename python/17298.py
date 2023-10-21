import sys

input = sys.stdin.readline

n = int(input().rstrip())

array = list(map(int, input().rstrip().split()))

result = [-1] * n
temp = []
for i in range(len(array)):
    while temp and array[temp[-1]] < array[i]:
        result[temp.pop()] = array[i]
    temp.append(i)
print(*result)