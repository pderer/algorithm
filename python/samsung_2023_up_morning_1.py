from collections import deque


n, m, k = map(int, input().split())
data = [] # 포탑 공격력 지도

is_active = [[False] * m for _ in range(n)]
for i in range(n):
    data.append(list(map(int, input().split())))

record =[[0] * m for _ in range(n)]
class Turret: # 클래스로 만들어서 정렬을 하자
    def __init__(self, x, y, rec, pow): # x, y, 공격한 시점, 공격력
        self.x = x
        self.y = y
        self.rec = rec
        self.pow = pow

live_turrets = []
turn = 0

def init():
    global turn
    
    turn += 1
    for i in range(n):
        for j in range(m):
            is_active[i][j] = False

def select_attacker():
    # 공격력이 가장 작은, 가장 최근에 공격한, 행과 열의 합이 가장 큰, 열 값이 가장 큰 순서대로 정렬  # noqa: E501
    live_turrets.sort(key = lambda x: (x.pow, -x.rec, -(x.x + x.y), -x.y))

    attacker = live_turrets[0]
    x = attacker.x
    y = attacker.y

    data[x][y] += n + m
    record[x][y] = turn
    attacker.pow = data[x][y]
    attacker.rec = record[x][y]
    is_active[x][y] = True

    live_turrets[0] = attacker

dx = [0, 1, 0, -1] # 우, 하, 좌, 상
dy = [1, 0, -1, 0]

def laser_attack():
    # 레이저 공격 먼저 시도
    attacker = live_turrets[0]
    attacker_x, attacker_y = attacker.x, attacker.y
    victim = live_turrets[-1]
    victim_x, victim_y = victim.x, victim.y
    visited = [[False] * m for _ in range(n)]
    back_x = [[0] * m for _ in range(n)] # 최단 경로에서 거쳐간 좌표 저장
    back_y = [[0] * m for _ in range(n)]
    visited[attacker_x][attacker_y] = True
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
    power = attacker.pow
    data[victim_x][victim_y] -= power
    is_active[victim_x][victim_y] = True
    if data[victim_x][victim_y] < 0:
        data[victim_x][victim_y] = 0
    x, y = back_x[victim_x][victim_y], back_y[victim_x][victim_y]
    while True:
        if x == attacker_x and y == attacker_y:
            break
        data[x][y] -= (power // 2)
        if data[x][y] < 0:
            data[x][y] = 0
        is_active[x][y] = True
        x, y = back_x[x][y], back_y[x][y]
    return True

dx2 = [-1, -1, -1, 0, 1, 1, 1, 0] # 8방향
dy2 = [-1, 0, 1, 1, 1, 0, -1, -1]

def bomb_attack():
    # 포탄 공격
    attacker = live_turrets[0]
    attacker_x, attacker_y = attacker.x, attacker.y
    victim = live_turrets[-1]
    victim_x, victim_y = victim.x, victim.y
    power = attacker.pow
    data[victim_x][victim_y] -= power
    is_active[victim_x][victim_y] = True
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
        data[nx][ny] -= (power // 2)
        is_active[nx][ny] = True
        if data[nx][ny] < 0:
            data[nx][ny] = 0

def fix():
    for i in range(n):
        for j in range(m):
            if is_active[i][j]:
                continue
            if data[i][j] == 0:
                continue
            data[i][j] += 1

for _ in range(k):
    live_turrets = []
    for i in range(n):
        for j in range(m):
            if data[i][j]:
                new_turret = Turret(i, j, record[i][j], data[i][j])
                live_turrets.append(new_turret)
    if len(live_turrets) <= 1:
        break
    init()
    select_attacker()
    if laser_attack() is False: # 레이저 공격 실패
        bomb_attack()
    fix()
    # print(data)

result = 0
for i in range(n):
    for j in range(m):
        result = max(result, data[i][j])
print(result)