# 2 ~ 7 -> 2
# 8 ~ 19 -> 3
# 20 ~ 37 -> 4
# 38 ~ 61 -> 5
# 62 ~ ? -> 6
# 6, 12, 18, 24, 30, 36, ... 6의 배수
# 1 까지는 1
# 1 + 6 = 7 까지는 2
# 1 + 6 + 12 = 19 까지는 3
# 1 + 6 + 12 + 18 = 37 까지는 4

n = int(input())
temp = 1
room = 1
while True:
    if n <= temp:
        print(room)
        break
    else:
        temp += 6 * room
        room += 1