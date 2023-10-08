from collections import deque


n, m, k = map(int, input().split())
data = [] # 포탑 공격력 지도

INF = 999999999
recent_attack = [] # 최근 공격한 포탑 (시점, x, y) 스택
is_active = [[False] * m for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)
    recent_attack.append((0, temp[0], temp[1]))

# 공격자 선정
def select_attcker(t): # t: 시점
    global n, m
    min_value = INF
    min_list = [] # (공격력, x, y)
    for i in range(n):
        for j in range(m):
            if 0 < data[i][j] <= min_value:
                min_value = data[i][j]
                min_list.append((min_value, i, j))
    min_value_list = []
    for element in min_list: # 공격력이 가장 낮은 포탑이 2개 이상인지 체크
        if element[0] == min_value:
            min_value_list.append((element[1], element[2])) # x, y 저장
    if len(min_value_list) > 1: # 공격력이 가장 낮은 포탑이 2개 이상
        # TODO: 가장 최근에 공격한 포탑 선택 return
        recent_list = []
        min_t = INF
        for recent in reversed(recent_attack): # stack 탐색
            for min in min_value_list:
                if recent[1] == min[0] and recent[2] == min[1]:
                    recent_list.append((recent[0], recent[1], recent[2]))

        if len(recent_list) > 1: # 가장 최근에 공격한 포탑이 2개 이상
            dup_recent_list = [] # 가장 최근 공격한 포탑이 중복될때 저장, 시간 차이가 상이  # noqa: E501
            for recent in recent_list:
                if t - recent[0] <= min_t:
                    min_t = t - recent[0]
                    dup_recent_list.append((min_t, recent[1], recent[2])) # 최소 시간, x, y  # noqa: E501
            real_dup_recent_list = [] # 가장 최근에 공격한 포탑, 시간 차이도 동일
            for recent in dup_recent_list:
                if recent[0] == min_t:
                    real_dup_recent_list.append((recent[1], recent[2])) # x, y

            if len(real_dup_recent_list) == 1: # 가장 최근에 공격한 포탑
                return (real_dup_recent_list[0], real_dup_recent_list[1]) # x, y
            
            # 가장 최근에 공격한 포탑이 2개 이상
            max = 0
            max_list = [] # max, x, y
            for recent in dup_recent_list:
                if recent[0] + recent[1] >= max:
                    max = recent[0] + recent[1]
                    max_list.append((max, recent[0], recent[1]))
            row_col_max_list = [] # 행과 열의 합이 가장 큰 값들을 저장
            if len(max_list) > 1: # 행과 열의 합이 가장 큰 값이 둘 이상
                for m in max_list:
                    if m[0] == max:
                        row_col_max_list.append((m[1], m[2]))
                if len(row_col_max_list) == 1: # 하나일때
                    return (row_col_max_list[0], row_col_max_list[1])
                col_max = 0
                return_x, return_y = 0, 0
                for m in row_col_max_list:
                    if m[1] > col_max:
                        return_x, return_y = m[0], m[1]
                return (return_x, return_y)
            else:
                return (max_list[0][0], max_list[0][1])
        else: # 가장 최근에 공격한 포탑이 하나
            return (recent_list[0][0], recent_list[0][1]) # x, y
    else: # 공격력이 가장 낮은 포탑이 하나
        return (min_value_list[0][0], min_value_list[0][1]) # x, y

def select_victim(t, x, y): # t: 시점, 공격자의 좌표
    global n, m
    max_value = 0
    max_list = []
    for i in range(n):
        for j in range(m):
            if i == x and j == y: # 공격자의 좌표인 경우
                continue
            if max_value < data[i][j]:
                max_value = data[i][j]
                max_list.append((max_value, i, j))
    max_value_list = []
    for max in max_list:
        if max[0] == max_value:
            max_value_list.append((max[1], max[2]))
    if len(max_value_list) > 1:
        latest_list = []
        max_t = 0
        for latest in recent_attack:
            for max in max_value_list:
                if latest[1] == max[0] and latest[2] == max[1]:
                    latest_list.append((latest[0], latest[1], latest[2]))
        if len(latest_list) > 1:
            dup_latest_list = [] # 가장 나중에 공격한 포탑이 중복될때 저장, 시간 차이가 상이  # noqa: E501
            for latest in latest_list:
                if t - latest[0] >= max_t:
                    max_t = t - latest[0]
                    dup_latest_list.append((max_t, latest[1], latest[2])) # 최대 시간, x, y  # noqa: E501
            real_dup_latest_list = [] # 가장 나중에 공격한 포탑, 시간 차이도 동일
            for latest in dup_latest_list:
                if latest[0] == max_t:
                    real_dup_latest_list.append((latest[1], latest[2])) # x, y

            if len(real_dup_latest_list) == 1: # 가장 최근에 공격한 포탑
                return (real_dup_latest_list[0], real_dup_latest_list[1]) # x, y
            
            # 가장 나중에 공격한 포탑이 2개 이상
            min = INF
            min_list = [] # max, x, y
            for latest in dup_latest_list:
                if latest[0] + latest[1] <= min:
                    min = latest[0] + latest[1]
                    min_list.append((min, latest[0], latest[1]))
            row_col_min_list = [] # 행과 열의 합이 가장 작은 값들을 저장
            if len(min_list) > 1: # 행과 열의 합이 가장 작은 값이 둘 이상
                for m in min_list:
                    if m[0] == min:
                        row_col_min_list.append((m[1], m[2]))
                if len(row_col_min_list) == 1: # 하나일때
                    return (row_col_min_list[0], row_col_min_list[1])
                col_min = INF
                return_x, return_y = 0, 0
                for m in row_col_min_list:
                    if m[1] < col_min:
                        return_x, return_y = m[0], m[1]
                return (return_x, return_y)
            else:
                return (min_list[0][0], min_list[0][1])
        else:
            return (latest_list[0][0], latest_list[0][1])
    else:
        return (max_value_list[0][0], max_value_list[0][1])

dx = [0, 1, 0, -1] # 우, 하, 좌, 상
dy = [1, 0, -1, 0]

def laser_attack(attacker_x, attacker_y, victim_x, victim_y):
    # 레이저 공격 먼저 시도
    visited = [[False] * m for _ in range(n)]
    back_x = [[0] * m for _ in range(n)] # 최단 경로에서 거쳐간 좌표 저장
    back_y = [[0] * m for _ in range(n)]
    visited[attacker_x][attacker_y] == 0
    queue = deque()
    queue.append((attacker_x, attacker_y))
    can_attack = False
    while queue:
        x, y = queue.popleft()
        if x == victim_x and y == victim_y:
            can_attack = True
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0:
                nx = n - 1
            if ny < 0:
                ny = m - 1
            if nx >= n:
                nx = 0
            if ny >= m:
                ny = 0
            if data[nx][ny] == 0: # 부서진 포탑
                continue
            if visited[nx][ny] is False:
                visited[nx][ny] = True
                back_x[nx][ny] = x
                back_y[nx][ny] = y
                queue.append((nx, ny))
    if can_attack is False:
        return False
    # 레이저 공격 시작
    attack = data[attacker_x][attacker_y]
    data[victim_x][victim_y] -= attack
    if data[victim_x][victim_y] < 0:
        data[victim_x][victim_y] = 0
    x, y = back_x[victim_x][victim_y], back_y[victim_x][victim_y]
    is_active[x][y] = True
    while True:
        if x == attacker_x and y == attacker_y:
            break
        data[x][y] -= (attack // 2)
        if data[x][y] < 0:
            data[x][y] = 0
        x, y = back_x[x][y], back_y[x][y]
        is_active[x][y] = True
    return True

dx2 = [-1, -1, -1, 0, 1, 1, 1, 0] # 8방향
dy2 = [-1, 0, 1, 1, 1, 0, -1, -1]

def bomb_attack(attacker_x, attacker_y, victim_x, victim_y):
    # 포탄 공격
    attack = data[attacker_x][attacker_y]
    data[victim_x][victim_y] -= attack
    if data[victim_x][victim_y] < 0:
        data[victim_x][victim_y] = 0
    for i in range(8):
        nx = victim_x + dx2[i]
        ny = victim_y + dy2[i]
        if nx < 0:
            nx = n - 1
        if ny < 0:
            ny = m - 1
        if nx >= n:
            nx = 0
        if ny >= m:
            ny = 0
        if data[nx][ny] == 0: # 부서진 포탑
            continue
        if nx == attacker_x and ny == attacker_y: # 공격자일 경우
            continue
        data[nx][ny] -= (attack // 2)
        is_active[nx][ny] = True
        if data[nx][ny] < 0:
            data[nx][ny] = 0

def fix():
    for i in range(n):
        for j in range(m):
            if is_active[i][j] is False:
                if data[i][j] != 0:
                    data[i][j] += 1

def init():
    for i in range(n):
        for j in range(m):
            is_active[i][j] = False

for i in range(1, k + 1):
    init()
    live = 0
    for j in range(n):
        for k in range(m):
            if data[j][k] > 0:
                live += 1
    if live <= 1:
        break
    attacker_x, attacker_y = select_attcker(i)
    print(attacker_x, attacker_y)
    data[attacker_x][attacker_y] += (n + m)
    is_active[attacker_x][attacker_y] = True
    victim_x, victim_y = select_victim(i, attacker_x, attacker_y)
    is_active[victim_x][victim_y] = True
    if laser_attack(attacker_x, attacker_y, victim_x, victim_y) is False: # 레이저 공격 실패  # noqa: E501
        bomb_attack(attacker_x, attacker_y, victim_x, victim_y)
    fix()
    print(data)

result = 0
for i in range(n):
    for j in range(m):
        result = max(result, data[i][j])
print(result)