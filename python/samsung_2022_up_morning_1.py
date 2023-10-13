from collections import deque

n, m, h, k = map(int, input().split())


class Person:
    def __init__(self, position, d):
        self.position = position
        self.d = d
        self.dead = False


graph = [[0] * n for _ in range(n)]
runners = []

# 도망자 좌표 설정, runners 리스트 초기화
for _ in range(m):
    temp = list(map(int, input().split()))
    for j in range(2):
        temp[j] -= 1
    runners.append(Person((temp[0], temp[1]), temp[2]))

# 나무 좌표 설정
for _ in range(h):
    temp = list(map(int, input().split()))
    temp[0] -= 1
    temp[1] -= 1
    graph[temp[0]][temp[1]] = 1

# 술래 좌표 설정
catcher = Person((n // 2, n // 2), 3)
# 술래가 방향 전환하기 전 이동한 거리
distance = 0
q = deque()
q.append(1)
q.append(1)

dx = [0, 0, 1, -1]  # 좌우하상 0123
dy = [-1, 1, 0, 0]

answer = 0


def run():
    cx, cy = catcher.position
    for i in range(m):
        runner = runners[i]
        if runner.dead:
            continue
        rx, ry = runner.position
        rd = runner.d

        # 술래와의 거리
        d_from_catcher = abs(rx - cx) + abs(ry - cy)

        # 술래와의 거리가 3 이하
        if d_from_catcher <= 3:
            nx = rx + dx[rd]
            ny = ry + dy[rd]
            # 현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나는 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                # 방향을 반대로
                if rd == 1:
                    rd = 0
                elif rd == 0:
                    rd = 1
                elif rd == 2:
                    rd = 3
                elif rd == 3: # 이것을 4라고 했었음
                    rd = 2
                runner.d = rd
                # 해당 위치에 술래가 없다면
                if (rx + dx[rd]) != cx or (ry + dy[rd]) != cy:
                    tx, ty = rx + dx[rd], ry + dy[rd]
                    runner.position = (tx, ty)

            # 격자를 벗어나지 않는 경우
            else:
                # 술래가 있지 않다면
                if (rx + dx[rd]) != cx or (ry + dy[rd]) != cy:
                    tx, ty = rx + dx[rd], ry + dy[rd]
                    runner.position = (tx, ty)


reverse = 0


def catcher_move():
    global distance, q, reverse
    cx, cy = catcher.position
    cd = catcher.d
    nx, ny = cx + dx[cd], cy + dy[cd]
    catcher.position = nx, ny
    distance += 1

    if nx == n // 2 and ny == n // 2:
        q.popleft()
        reverse = 0
        distance = 0
        # 위를 바라보도록
        catcher.d = 3
        q.append(1)
        q.append(1)

    elif distance == q[0]:
        previous = q.popleft()
        # 방향 전환 해야 함
        distance = 0
        # 시계 방향
        if reverse == 0:
            if cd == 3:
                cd = 1
            elif cd == 1:
                cd = 2
            elif cd == 2:
                cd = 0
            elif cd == 0:
                cd = 3
        # 반시계 방향
        elif reverse == 1:
            if cd == 2:
                cd = 1
            elif cd == 1:
                cd = 3
            elif cd == 3:
                cd = 0
            elif cd == 0:
                cd = 2
        # 방향 업데이트
        catcher.d = cd
        # 큐 가 비어 있으면
        if not q and reverse == 0:
            # 그 이전 값보다 1 큰 값으로 두개 추가
            q.append(previous + 1)
            q.append(previous + 1)
        elif not q and reverse == 1:
            q.append(previous - 1)
            q.append(previous - 1)

    # 1행 1열 도착
    elif nx == 0 and ny == 0:
        q.popleft()
        q.popleft()
        # 방향 전환
        reverse = 1
        distance = 0
        # 밑을 바라보도록
        catcher.d = 2
        q.append(n - 1)
        q.append(n - 1)
        q.append(n - 1)


def graph_check(x, y):
    return not(x < 0 or y < 0 or x >= n or y >= n)


def catch():
    global time, answer
    cx, cy = catcher.position
    cd = catcher.d
    count = 0
    if cd == 0:
        for j in range(2, -1, -1):  # 2, 1, 0
            if graph_check(cx, cy - j):
                if graph[cx][cy - j] == 1:
                    continue
                for index in range(m):
                    runner = runners[index]
                    rx, ry = runner.position
                    if rx == cx and ry == cy - j and not runner.dead:
                        runner.dead = True
                        count += 1
    elif cd == 1:
        for j in range(3):  # 0, 1, 2
            if graph_check(cx, cy + j):
                if graph[cx][cy + j] == 1:
                    continue
                for index in range(m):
                    runner = runners[index]
                    rx, ry = runner.position
                    if rx == cx and ry == cy + j and not runner.dead:
                        runner.dead = True
                        count += 1
    elif cd == 2:
        for i in range(3):  # 0, 1, 2
            if graph_check(cx + i, cy):
                if graph[cx + i][cy] == 1:
                    continue
                for index in range(m):
                    runner = runners[index]
                    rx, ry = runner.position
                    if rx == cx + i and ry == cy and not runner.dead:
                        runner.dead = True
                        count += 1
    elif cd == 3:
        for i in range(2, -1, -1):  # 2, 1, 0
            if graph_check(cx - i, cy):
                if graph[cx - i][cy] == 1:
                    continue
                for index in range(m):
                    runner = runners[index]
                    rx, ry = runner.position
                    if rx == cx - i and ry == cy and not runner.dead:
                        runner.dead = True
                        count += 1
    answer += time * count


time = 0
for _ in range(k):
    time += 1
    run()
    catcher_move()
    catch()

print(answer)