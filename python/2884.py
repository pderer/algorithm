h, m = map(int, input().split())

if m - 45 < 0:
    h -= 1
    m = 60 + (m - 45)
    if h < 0:
        h = 23
    print(h, m)
else:
    print(h, m - 45)