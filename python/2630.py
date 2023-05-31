import sys

b = 0
w = 0


def cut(list):
    l = len(list)
    if list == [[0 for _ in range(l)] for _ in range(l)]:
        global w
        w += 1
    elif list == [[1 for _ in range(l)] for _ in range(l)]:
        global b
        b += 1
    elif l == 1:
        return
    else:
        temp_len = int(l/2)
        temp1 = [[0 for _ in range(temp_len)] for _ in range(temp_len)]
        temp2 = [[0 for _ in range(temp_len)] for _ in range(temp_len)]
        temp3 = [[0 for _ in range(temp_len)] for _ in range(temp_len)]
        temp4 = [[0 for _ in range(temp_len)] for _ in range(temp_len)]
        for i in range(temp_len):
            for j in range(temp_len):
                temp1[i][j] = list[i][j]
        for i in range(temp_len):
            for j in range(temp_len, l):
                temp2[i][j-temp_len] = list[i][j]
        for i in range(temp_len, l):
            for j in range(temp_len):
                temp3[i-temp_len][j] = list[i][j]
        for i in range(temp_len, l):
            for j in range(temp_len, l):
                temp4[i-temp_len][j-temp_len] = list[i][j]
        cut(temp1)
        cut(temp2)
        cut(temp3)
        cut(temp4)


n = int(input())
list = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    temp = sys.stdin.readline().split()
    for j in range(n):
        list[i][j] = int(temp[j])
cut(list)
print(w)
print(b)
