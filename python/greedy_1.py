N, M, K = map(int, input().split())
result = 0
count = 0
array = input().split()
array = list(map(int, array))
array.sort()

first = array[-1]
second = array[-2]

while True:
    for i in range(K):
        result += first
        count += 1
        if count == M:
            break
    result += second
    count += 1
    if count == M:
        break

print(result)
    