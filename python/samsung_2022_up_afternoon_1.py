n, m, k = map(int, input().split())
graph = [[0] * (n + 1)]  # 모든 index 1 부터 시작 하자 헷갈 리지 않게, y축 하나 추가 한 것 리스트, 이미 x 축 하나 추가됨  # noqa: E501
for _ in range(n):
    graph.append([0] + list(map(int, input().split())))  # y축 하나 추가 한 것

v = [[] for _ in range(m + 1)]
# 각 팀별 tail 위치를 관리함 -> 팀원의 크기는 변하지 않으므로 꼬리 위치는 불변
tail = [0] * (m + 1)
visited = [[False] * (n + 1) for _ in range(n + 1)]
graph_idx = [[0] * (n + 1) for _ in range(n + 1)]
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
answer = 0


def find_teams():
    cnt = 1

    for x in range(n + 1):
        for y in range(n + 1):
            if graph[x][y] == 1:
                v[cnt].append((x, y))
                cnt += 1

    for i in range(1, m + 1):
        x, y = v[i][0]
        dfs(x, y, i)


def is_out_range(x, y):
    return not (1 <= x <= n and 1 <= y <= n)


def dfs(x, y, idx):
    visited[x][y] = True
    graph_idx[x][y] = idx
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_out_range(nx, ny):
            continue
        if graph[nx][ny] == 0:
            continue
        if visited[nx][ny]:
            continue

        # 가장 처음 탐색할 때 2가 있는 방향으로 dfs 진행 -> 자동으로 3까지 탐색, 그 이후 4도 v에 추가함  # noqa: E501
        if len(v[idx]) == 1 and graph[nx][ny] != 2:
            continue

        v[idx].append((nx, ny))
        if graph[nx][ny] == 3:
            tail[idx] = len(v[idx])
        dfs(nx, ny, idx)


def move():
    for i in range(1, m + 1):
        # 각 팀에 대해 레일을 한 칸씩 뒤로 이동
        tmp = v[i][-1]  # 맨 뒤 칸
        for j in range(len(v[i]) - 1, 0, -1):  # 맨 뒤에서 index 1까지 (index 0은 tmp로 저장함)  # noqa: E501
            v[i][j] = v[i][j - 1]
        v[i][0] = tmp  # 맨 앞에 맨 뒤였던 거 저장

    for i in range(1, m + 1):
        for j, (x, y) in enumerate(v[i]):
            if j == 0:  # 레일의 맨 앞 -> 머리
                graph[x][y] = 1
            elif j < tail[i] - 1:
                graph[x][y] = 2
            elif j == tail[i] - 1:
                graph[x][y] = 3
            else:
                graph[x][y] = 4


def get_point(x, y):
    global answer
    idx = graph_idx[x][y]
    cnt = v[idx].index((x, y))
    answer += (cnt + 1) * (cnt + 1)


time = 0


def throw_ball():
    t = (time - 1) % (4 * n) + 1

    if t <= n:
        # 1 ~ n 라운드의 경우 왼쪽에서 오른쪽 방향으로 공을 던집니다.
        for i in range(1, n + 1):
            if 1 <= graph[t][i] and graph[t][i] <= 3:
                # 사람이 있는 첫 번째 지점을 찾습니다.
                # 찾게 되면 점수를 체크한 뒤 찾은 사람의 팀 번호를 저장합니다.
                get_point(t, i)
                return graph_idx[t][i]
    elif t <= 2 * n:
        # n+1 ~ 2n 라운드의 경우 아래에서 윗쪽 방향으로 공을 던집니다.
        t -= n
        for i in range(1, n + 1):
            if 1 <= graph[n + 1 - i][t] and graph[n + 1 - i][t] <= 3:
                # 사람이 있는 첫 번째 지점을 찾습니다.
                # 찾게 되면 점수를 체크한 뒤 찾은 사람의 팀 번호를 저장합니다.
                get_point(n + 1 - i, t)
                return graph_idx[n + 1 - i][t]
    elif t <= 3 * n:
        # 2n+1 ~ 3n 라운드의 경우 오른쪽에서 왼쪽 방향으로 공을 던집니다.
        t -= (2 * n)
        for i in range(1, n + 1):
            if 1 <= graph[n + 1 - t][n + 1 - i] and graph[n + 1 - t][n + 1 - i] <= 3:
                # 사람이 있는 첫 번째 지점을 찾습니다.
                # 찾게 되면 점수를 체크한 뒤 찾은 사람의 팀 번호를 저장합니다.
                get_point(n + 1 - t, n + 1 - i)
                return graph_idx[n + 1 - t][n + 1 - i]
    else:
        # 3n+1 ~ 4n 라운드의 경우 위에서 아랫쪽 방향으로 공을 던집니다.
        t -= (3 * n)
        for i in range(1, n + 1):
            if 1 <= graph[i][n + 1 - t] and graph[i][n + 1 - t] <= 3:
                # 사람이 있는 첫 번째 지점을 찾습니다.
                # 찾게 되면 점수를 체크한 뒤 찾은 사람의 팀 번호를 저장합니다.
                get_point(i, n + 1 - t)
                return graph_idx[i][n + 1 - t]

    # 공이 그대로 지나간다면 0을 반환합니다.
    return 0


def reverse(idx):
    if idx == 0:
        return

    new_v = []

    for j in range(tail[idx] - 1, -1, -1):  # 1 2 3 -> 3 2 1
        new_v.append(v[idx][j])

    for j in range(len(v[idx]) - 1, tail[idx] - 1, -1):  # 1 2 3 4 4 4 4 -> 3 2 1 4 4 4 4  # noqa: E501
        new_v.append(v[idx][j])

    v[idx] = new_v[:]

    for j, (x, y) in enumerate(v[idx]):
        if j == 0:
            graph[x][y] = 1
        elif j < tail[idx] - 1:
            graph[x][y] = 2
        elif j == tail[idx] - 1:
            graph[x][y] = 3
        else:
            graph[x][y] = 4


find_teams()


for _ in range(k):
    time += 1
    move()
    got_ball_idx = throw_ball()
    reverse(got_ball_idx)

print(answer)
