from sys import stdin

n, m = map(int, stdin.readline().split())

nums = list(map(int, stdin.readline().split()))

temp = 0

accum_list = [0] * (n + 1)

for i in range(n):
    temp += nums[i]
    accum_list[i + 1] = temp

for i in range(m):
    start, end = map(int, stdin.readline().split())
    print(accum_list[end] - accum_list[start - 1])