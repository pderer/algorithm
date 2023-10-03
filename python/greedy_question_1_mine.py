n = int(input())

array = list(map(int, input().split()))
array.sort(reverse=True) # 내림차순

max = array[0]
result = 1
index = 0
while True:
    index += max
    if index > n - 1:
        break
    max = array[index]
    result += 1
    
print(result)