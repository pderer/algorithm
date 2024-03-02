n = int(input())

nums = list(map(int, input().split()))

compressed = sorted(set(nums))

dict = {}

for i in range(len(compressed)):
    dict[compressed[i]] = i

for i in range(n):
    print(dict[nums[i]], end=" ")