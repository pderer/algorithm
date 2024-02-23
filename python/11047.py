n, k = map(int, input().split())

coins = []

max = 0
count = 0
index = 0
sum = 0
for i in range(n):
    temp = int(input())
    if temp > max and temp <= k:
        max = temp
        index = i
    coins.append(temp)

while sum < k:
    temp_count = (k - sum) // max
    count += temp_count
    sum += temp_count * max
    index -= 1
    max = coins[index]

print(count)