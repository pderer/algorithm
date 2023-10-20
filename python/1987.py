r, c = map(int, input().split())

alphabet = []
for _ in range(r):
    alphabet.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 1
def bfs(x, y):
    global answer
    q = set([(x, y, alphabet[x][y])])
    while q:
        x, y, ans = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if alphabet[nx][ny] not in ans:
                q.add(nx, ny, ans + alphabet[nx][ny])
                answer = max(answer, len(ans) + 1)

bfs(0, 0)
print(answer)