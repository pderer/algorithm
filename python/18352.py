from collections import deque


n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)] # 0 ~ n 의 노드 표현

distance = [-1] * (n + 1)

for i in range(m):
    temp = list(map(int, input().split()))
    graph[temp[0]].append(temp[1])

def bfs(start):
    queue = deque([start])
    distance[start] = 0 # 방문 처리
    while queue:
        v = queue.popleft()
        for near in graph[v]: # 인접 노드
            if distance[near] == -1: # 방문하지 않은 노드
                distance[near] = distance[v] + 1
                queue.append(near)

bfs(x)

check = False
for i in range(len(distance)):
    if distance[i] == k:
        check = True
        print(i)

if check is False:
    print(-1)