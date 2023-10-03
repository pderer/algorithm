n = input()

sum1 = 0
sum2 = 0

for i in range(int(len(n) / 2)):
    sum1 += int(n[i])
    sum2 += int(n[i + int(len(n) / 2)])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")