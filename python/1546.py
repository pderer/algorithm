n = int(input())
nums = list(map(int, input().split()))
temps = [0] * n

maximum = max(nums)
for i in range(n):
    temps[i] = nums[i] / maximum * 100

mean = sum(temps) / n
print(mean)