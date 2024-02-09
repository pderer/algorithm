checks = [False] * 42

for i in range(10):
    n = int(input())
    checks[n % 42] = True

cnt = 0
for check in checks:
    if check is True:
        cnt += 1
print(cnt)
