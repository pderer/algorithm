n, m = map(int, input().split())
a, b, d = map(int, input().split())
mapping = []

forwards = [(-1, 0), (0, 1), (1, 0), (0, -1)]
backwards = [(1, 0), (0, -1), (-1, 0), (0, 1)]

for i in range(n):
    mapping.append(list(map(int, input().split())))

mapping[a][b] = -1

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

visit = 0
turn_time = 0
while True:
    # 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다
    # -> 일단 왼쪽으로 돌아
    turn_left()
    # 그 방향으로 아직 가보지 않은 칸이 존재한다면, 한 칸 전진
    if mapping[a + forwards[d][0]][b + forwards[d][1]] == 0:
        mapping[a][b] = -1
        a = a + forwards[d][0]
        b = b + forwards[d][1]
        visit += 1
        turn_time = 0 # 왜 0으로 초기화? -> 이동하면 다시 처음부터 왼쪽으로 돈다 (1단계로 돌아간다)  # noqa: E501
        continue
    # 가본 칸이거나 바다인 칸인 경우, turn time 증가
    else:
        turn_time += 1
    # 모든 방향으로 돌아본 경우, 방향을 유지한 채로 한 칸 뒤로 간다.
    # 뒤쪽 칸이 바다인 경우, 움직임을 멈춤
    if turn_time == 4:
        if mapping[a + backwards[d][0]][b + backwards[d][1]] == -1:
            mapping[a][b] = -1
            a = a + backwards[d][0]
            b = b + backwards[d][1]
            turn_time = 0
            visit += 1
        if mapping[a + backwards[d][0]][b + backwards[d][1]] == 1:
            break

print(visit)
print(mapping)