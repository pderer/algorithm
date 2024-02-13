from math import factorial

n = int(input())
fact = factorial(n)
count = 0

for s in reversed(str(fact)):
    if s == '0':
        count += 1
    else:
        break
print(count)