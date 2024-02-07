n, k = map(int, input().split())

nums = list(input())

temp = []

deleted = 0
for i in range(len(nums)):
    while temp and temp[-1] < nums[i] and deleted < k:
        temp.pop()
        deleted += 1
    temp.append(nums[i])

if deleted < k:
    print(''.join(temp[:n-k]))
else:
    print(''.join(temp))