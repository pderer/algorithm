n, m = map(int, input().split())

plus = []
minus = []

temp = list(map(int, input().split()))

for i in range(n):
    if temp[i] > 0:
        plus.append(temp[i])
    else:
        minus.append(-temp[i])

plus.sort(reverse=True)
minus.sort(reverse=True)

total = 0

for i in range(0, len(plus), m):
    total += 2 * plus[i]

for i in range(0, len(minus), m):
    total += 2 * minus[i]

if not plus:
    total -= minus[0]
elif not minus:
    total -= plus[0]
else:
    total -= max(plus[0], minus[0])

print(total)