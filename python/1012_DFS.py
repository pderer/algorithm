import sys

sys.setrecursionlimit(10000)

total = int(sys.stdin.readline())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def DFS(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if table[nx][ny] == 1:
                table[nx][ny] = 0
                DFS(nx, ny)
    return


for i in range(total):
    counter = 0
    m, n, k = map(int, sys.stdin.readline().split())
    table = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        table[y][x] = 1
    for a in range(n):
        for b in range(m):
            if table[a][b] == 1:
                DFS(a, b)
                counter += 1
    print(counter)
