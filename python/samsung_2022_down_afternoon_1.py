from collections import deque


n, m = map(int, input().split())

# 좌표 index는 0부터 시작한다고 가정
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

store = [(-1, -1)] # m 개의 편의점, index 0은 쓰레기값
for i in range(m):
    temp = list(map(int, input().split()))
    for j in range(2):
        temp[j] -= 1
    store.append(tuple(temp))

# 사람도 m명, index 0은 쓰레기 값
persons = [(-1, -1) for _ in range(m + 1)]
t = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def move():
    for i in range(1, m + 1):
        px, py = persons[i]
        if px == -1 and py == -1: # 격자 밖이라면
            continue
        if persons[i] == store[i]: # 이거 생각안해서 고생함
            continue
        
        visited = [[False] * n for _ in range(n)] # BFS
        distance = [[0] * n for _ in range(n)]
        back_x = [[0] * n for _ in range(n)]
        back_y = [[0] * n for _ in range(n)]

        px, py = persons[i]
        sx, sy = store[i]
        q = deque()
        q.append((px, py))
        visited[px][py] = True

        while q: # 편의점에서 출발 -> 현재 사람의 위치
            qx, qy = q.popleft()
            if qx == sx and qy == sy: # 편의점 좌표
                break
            for j in range(4): # i 안에 i 써서 고생함
                nx = qx + dx[j]
                ny = qy + dy[j]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if graph[nx][ny] == -1: # 해당 칸 지나갈 수 없음
                    continue
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                distance[nx][ny] = distance[qx][qy] + 1
                q.append((nx, ny))
                back_x[nx][ny] = qx
                back_y[nx][ny] = qy
        
        tx, ty = back_x[sx][sy], back_y[sx][sy]
        if tx == px and ty == py:
            persons[i] = (sx, sy)
            continue # break 했어서 고생함
        
        while True:
            if back_x[tx][ty] == px and back_y[tx][ty] == py:
                break
            else:
                ttx, tty = tx, ty
                tx, ty = back_x[ttx][tty], back_y[ttx][tty]
        
        persons[i] = (tx, ty)
    
    # 격자안의 모든 사람이 이동 후
    for i in range(1, m + 1):
        if store[i] == persons[i]:
            px, py = persons[i]
            graph[px][py] = -1


def enter_base():
    visited = [[False] * n for _ in range(n)] # BFS
    distance = [[0] * n for _ in range(n)]

    # t번 편의점, t번 사람
    if t <= m and persons[t] == (-1, -1): # -1, -1이 아니라면 이미 베이스캠프에 들어간 것임  # noqa: E501
        sx, sy = store[t]
        q = deque()
        q.append((sx, sy))
        visited[sx][sy] = True

        basecamps = []
        while q:
            qx, qy = q.popleft()
            if graph[qx][qy] == 1: # 베이스캠프 좌표
                basecamps.append((qx, qy, distance[qx][qy])) # x, y, 최단 거리
            for i in range(4):
                nx = qx + dx[i]
                ny = qy + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if graph[nx][ny] == -1: # 해당 칸 지나갈 수 없음
                    continue
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                distance[nx][ny] = distance[qx][qy] + 1
                q.append((nx, ny))
        
        basecamps.sort(key = lambda x: (x[2], x[0], x[1])) # 최단 거리, 열, 행
        bx, by, d = basecamps[0]

        persons[t] = (bx, by)

        # 어차피 한번 밖에 안함
        graph[bx][by] = -1

while True:
    t += 1
    
    move()
    enter_base()
    
    # 모든 사람이 편의점에 도착할 경우 break
    all_arrived = True
    for i in range(1, m + 1):
        if store[i] != persons[i]:
            all_arrived = False
    
    if all_arrived:
        break
    
print(t)

    