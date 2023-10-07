from collections import deque


n, k = map(int, input().split())
graph = []
data = [] # 바이러스의 정보를 담음, (종류, 시간, x, y)

for i in range(n):
    temp_list = list(map(int, input().split()))
    graph.append(temp_list)
    for j in range(len(temp_list)):
        if temp_list[j] != 0:
            data.append((graph[i][j], 0, i, j)) # 큐에 좌표 말고 다른 정보들을 넣어서 활용할 수 있음  # noqa: E501

data.sort() # 튜플을 가지는 리스트를 정렬하면 가장 왼쪽에 있는 값 기준으로 정렬
queue = deque(data) # deque 파라미터를 리스트로 줘서 정의할 수 있음

target_s, target_x, target_y = map(int, input().split()) # x, y index 주의, 1 부터 시작

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue: # BFS 중에 전역 변수를 활용하고 싶다면 함수를 안 사용해도 됨
    virus, s, x, y = queue.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            queue.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])