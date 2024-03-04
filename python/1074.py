n, r, c = map(int, input().split())

if n == 1:
    if r == 0 and c == 0:
        print(0)
    elif r == 0 and c == 1:
        print(1)
    elif r == 1 and c == 0:
        print(2)
    else:
        print(3)
    exit(0)

temp_r, temp_c = 0, 0
count = 0

while n > 0:
    temp_r, temp_c = r // (2 ** (n - 1)), c // (2 ** (n - 1))
    if temp_r == 0 and temp_c == 0:
        pass
    elif temp_r == 0 and temp_c == 1:
        count += 4 ** (n - 1)
    elif temp_r == 1 and temp_c == 0:
        count += 2 * (4 ** (n - 1))
    else:
        count += 3 * (4 ** (n - 1))
    r, c = r % (2 ** (n - 1)), c % (2 ** (n - 1))
    n -= 1
print(count)