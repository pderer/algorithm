r, c = map(int, input().split())

alphabet = []
for _ in range(r):
    alphabet.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
check = [False] * 26
answer = 0
def dfs(x, y, cnt):
    global answer
    answer = max(cnt, answer)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if check[ord(alphabet[nx][ny]) - 65] is False:
            check[ord(alphabet[nx][ny]) - 65] = True
            ncnt = cnt + 1
            dfs(nx, ny, ncnt)
            check[ord(alphabet[nx][ny]) - 65] = False

check[ord(alphabet[0][0]) - 65] = True
dfs(0, 0, 1)
print(answer)