n, m, k = map(int, input().split())

graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
for i in range(1, n + 1):
    graph[i] = [0] + list(map(int, input().split()))


players = [(-1, -1)] + [
    tuple(map(int, input().split()))
    for _ in range(m)
]
 # 참가자 좌표 리스트

escapes = tuple(map(int, input().split())) # 탈출 좌표
ans = 0

r, c, square_size = 0, 0, 0


def move():
    global escapes, ans
    
    for i in range(1, m + 1):
        if players[i] == escapes:
            continue

        px, py = players[i]
        ex, ey = escapes
    
        if px != ex:
            nx, ny = px, py

            if ex > nx:
                nx += 1
            else:
                nx -= 1

            if not graph[nx][ny]:
                players[i] = (nx, ny)
                ans += 1
                continue
        
        if py != ey:
            nx, ny = px, py

            if ey > ny:
                ny += 1
            else:
                ny -= 1
            
            if not graph[nx][ny]:
                players[i] = (nx, ny)
                ans += 1
                continue

def find_square():
    global escapes, r, c, square_size

    ex, ey = escapes
    for size in range(2, n + 1):   
        for i in range(1, n + 2 - size):
            for j in range(1, n + 2 - size):
                x, y = i + size - 1, j + size - 1
                if not (i <= ex <= x and j <= ey <= y):
                    continue
                have_player = False
                for l in range(1, m + 1):  # noqa: E741
                    px, py = players[l]
                    if i <= px <= x and j <= py <= y:
                        if not (px == ex and py == ey):
                            have_player = True
                if have_player:
                    r = i
                    c = j
                    square_size = size
                    return
            
def turn():
    global escapes, r, c, square_size

    temp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(r, r + square_size):
        for j in range(c, c + square_size):
            if graph[i][j]:
                graph[i][j] -= 1

    for i in range(r, r + square_size):
        for j in range(c, c + square_size):
            ox, oy = i - r, j - c
            rx, ry = oy, square_size - ox - 1
            temp[r + rx][c + ry] = graph[i][j]
    
    for i in range(r, r + square_size):
        for j in range(c, c + square_size):
            graph[i][j] = temp[i][j]

    for i in range(1, m + 1):
        px, py = players[i]
        if r <= px < r + square_size and c <= py < c + square_size:
            ox, oy = px - r, py - c
            rx, ry = oy, square_size - ox - 1
            players[i] = (rx + r, ry + c)
    
    ex, ey = escapes
    if r <= ex < r + square_size and c <= ey < c + square_size:
        ox, oy = ex - r, ey - c
        rx, ry = oy, square_size - ox - 1
        escapes = (rx + r, ry + c)
    

# k 초 동안 시뮬레이션
for _ in range(k):

    # 한칸씩 움직임
    move()

    is_all_escaped = True
    for i in range(1, m + 1):
        if players[i] != escapes:
            is_all_escaped = False
    
    if is_all_escaped:
        break

    find_square()
    turn()

print(ans)

ex, ey = escapes
print(ex, ey)