n = int(input()) # 보드 한 변의 길이
board = [[0] * n for _ in range(n)]

k = int(input()) # 사과의 개수
apple_map = []
for i in range(k):
    temp = list(map(int, input().split()))
    board[temp[0] - 1][temp[1] - 1] = -1

l = int(input()) # 방향 변환 횟수  # noqa: E741

turn_map = []
for i in range(l):
    turn_map.append(list(input().split()))

dx = [0, 1, 0, -1] # 우, 하, 좌, 상
dy = [1, 0, -1, 0]

head_direction = 0 # 머리 방향 처음은 우
head_x, head_y = 0, 0 # 머리의 처음 좌표는 맨 위, 맨 좌측
q = [(head_x, head_y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
board[0][0] = 1 # 처음 좌표는 뱀 처리 (1)
time = 0

def move(direction, x, y):
    nx = x + dx[direction]
    ny = y + dy[direction]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        return False # 벽에 부딪힘
    # TODO : 자기 몸 부딪힘
    if board[nx][ny] != -1 and board[nx][ny] == 1: # 사과가 있는 곳이 아니고, 자기 몸일 경우  # noqa: E501
        return False
    return nx, ny

def eat(x, y):
    if board[x][y] == -1: # 이동한 칸에 사과가 있다면
        return True
    else: # 이동한 칸에 사과가 없음
        return False

def turn_head(time):
    global head_direction
    for turn in turn_map:
        if time == int(turn[0]): # 방향 전환할 시간일 경우
            if turn[1] == 'D': # 오른쪽
                head_direction += 1
                if head_direction > 3:
                    head_direction = 0
            else: # 왼쪽
                head_direction -= 1
                if head_direction < 0:
                    head_direction = 3
    
while True:
    # 매 초마다 이동
    time += 1
    # 머리를 다음 칸에 위치
    if move(head_direction, head_x, head_y) is False:
        print(time)
        break
    new_head_x, new_head_y = move(head_direction, head_x, head_y)
    if eat(new_head_x, new_head_y) is False: # 사과 못 먹음
        board[new_head_x][new_head_y] = 1
        q.append((new_head_x, new_head_y))
        old_tail_x, old_tail_y = q.pop(0)
        board[old_tail_x][old_tail_y] = 0
    else: # 사과 먹음
        board[new_head_x][new_head_y] = 1 # 머리
        q.append((new_head_x, new_head_y))
    head_x, head_y = new_head_x, new_head_y
    turn_head(time)