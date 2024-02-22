n = int(input())
nums = [0] * 10000
for _ in range(n):
    nums[int(input()) - 1] += 1

for i in range(len(nums)):
    for _ in range(nums[i]):
        print(i + 1)