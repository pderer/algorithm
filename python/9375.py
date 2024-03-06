t = int(input())

for _ in range(t):
    n = int(input())
    dict = {}
    for _ in range(n):
        _, category = input().split()
        
        if category in dict:
            dict[category] += 1
        else:
            dict[category] = 2
        
    count = 1
    for temp in dict.values():
        count *= temp
    print(count - 1)
