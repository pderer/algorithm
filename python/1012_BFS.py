import sys
from collections import deque

total = int(sys.stdin.readline())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def BFS(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                if table[nx][ny] == 1:
                    table[nx][ny] = 0
                    queue.append((nx, ny))
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
                BFS(a, b)
                counter += 1
    print(counter)
