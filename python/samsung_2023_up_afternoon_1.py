from collections import deque


n, m, k = map(int, input().split())
graph = [] # 미로 정보
for i in range(n):
    graph.append(list(map(int, input().split())))

players = [] # 참가자 좌표 리스트
for i in range(m):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        temp[j] -= 1
    players.append(temp)

escape_x, escape_y = map(int, input().split()) # 탈출 좌표

# 전처리
escape_x -= 1
escape_y -= 1

# 정사각형 클래스
class Square:
    def __init__(self, size, r, c):
        self.size = size
        self.r = r
        self.c = c

def move2(player_x, player_y):
    global escape_x, escape_y
    
    if escape_x != player_x:
        nx, ny = player_x, player_y

        if escape_x > nx:
            nx += 1
        else:
            nx -= 1

        if not graph[nx][ny]:
            return (nx, ny)
    
    if escape_y != player_y:
        nx, ny = player_x, player_y

        if escape_y > ny:
            ny += 1
        else:
            ny -= 1
        
        if not graph[nx][ny]:
            return (nx, ny)
    return (-1, -1)

def turn(square):
    global escape_x, escape_y, players

    size, r, c = square.size, square.r, square.c
    temp = [[0] * n for _ in range(n)]
    for i in range(r, r + size):
        for j in range(c, c + size):
            if graph[i][j] > 0:
                graph[i][j] -= 1

    for i in range(r, r + size):
        for j in range(c, c + size):
            ox, oy = i - r, j - c
            rx, ry = oy, size - ox - 1
            temp[r + rx][c + ry] = graph[i][j]
    
    for i in range(r, r + size):
        for j in range(c, c + size):
            graph[i][j] = temp[i][j]

    for i in range(len(players)):
        px = players[i][0]
        py = players[i][1]
        if r <= px < r + size and c <= py < c + size:
            ox, oy = px - r, py - c
            rx, ry = oy, size - ox - 1
            players[i][0] = rx + r
            players[i][1] = ry + c
    
    if r <= escape_x < r + size and c <= escape_y < c + size:
        ox, oy = escape_x - r, escape_y - c
        rx, ry = oy, size - ox - 1
        escape_x, escape_y = rx + r, ry + c
    
    # print(graph)
    # print(escape_x, escape_y)

moved_distance = 0
# k 초 동안 시뮬레이션
for _ in range(k):

    # 한칸씩 움직임
    removed_list = []
    for i in range(len(players)):
        temp_x, temp_y = move2(players[i][0], players[i][1])
        if temp_x == -1 and temp_y == -1: # 움직임이 없음
            continue
        players[i][0] = temp_x
        players[i][1] = temp_y
        moved_distance += 1
        if players[i][0] == escape_x and players[i][1] == escape_y:
            removed_list.append(i)
            continue
    print(players)
    print(escape_x, escape_y)
    print(graph)
    # 탈출한 참가자 삭제
    for index in removed_list:
        print(removed_list)
        print(index)
        del players[index]

    # 모두가 탈출했다면
    if len(players) == 0:
        break

    # 가능한 모든 정사각형 리스트 만들기
    square_list = []
    for size in range(2, n + 1):   
        for i in range(n + 2 - size):
            for j in range(n + 2 - size):
                x, y = i + size - 1, j + size - 1
                if not (i <= escape_x <= x and j <= escape_y <= y):
                    continue
                have_player = False
                for player in players:
                    tx, ty = player[0], player[1]
                    if i <= tx <= x and j <= ty <= y:
                        if not (tx == escape_x and ty == escape_y):
                            have_player = True
                if have_player:
                    square_list.append(Square(size, i, j))
    square_list.sort(key = lambda x: (x.size, x.r, x.c))
    selected_square = square_list[0] # 선택된 정사각형
    print(f"square: {selected_square.size}, {selected_square.r}, {selected_square.c}")
    
    turn(selected_square)
    print("after turn")
    print(players)
    print(escape_x, escape_y)
    print(graph)
    print("-----------")

print(moved_distance)
print(escape_x + 1, escape_y + 1)