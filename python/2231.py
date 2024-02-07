n = int(input())
check = False
for i in range(1, n):
    temp = i
    for s in str(i):
        temp += int(s)
    if temp == n:
        check = True
        print(i)
        break
if check is False:
    print(0)