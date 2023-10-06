from itertools import combinations


n, m = map(int, input().split())
data = []
zero_list = []
virus_list = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 0:
            zero_list.append((i, j))
        elif temp[j] == 2:
            virus_list.append((i, j))
    data.append(temp)

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if data[nx][ny] == 0:
            data[nx][ny] = 2
            dfs(nx, ny)

normal_list = []
wall_list = list(combinations(zero_list, 3))

for wall in wall_list: # 모든 조합에 대해
    data[wall[0][0]][wall[0][1]] = 1 # 벽 만들기
    data[wall[1][0]][wall[1][1]] = 1
    data[wall[2][0]][wall[2][1]] = 1
    
    for virus in virus_list:
        dfs(virus[0], virus[1]) # 바이러스 퍼뜨리기
    
    temp = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0: # 안전 구역 구하기
                temp += 1
    normal_list.append(temp)

    # 다시 data 초기화
    data = [[1] * m for _ in range(n)]
    for zero in zero_list:
        data[zero[0]][zero[1]] = 0
    for virus in virus_list:
        data[virus[0]][virus[1]] = 2

print(max(normal_list))
