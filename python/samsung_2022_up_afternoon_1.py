from collections import deque

n, m, k = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


class Team:
    def __init__(self, persons, point):
        self.persons = persons  # person list
        self.point = point  # 점수


class Person:
    def __init__(self, position, role):
        self.position = position  # 좌표
        self.role = role  # 역할 (머리, 몸통, 꼬리)


visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
team_list = []


def find_teams():
    global team_list

    for x in range(n):
        for y in range(n):
            if graph[x][y] != 1:
                continue
            if visited[x][y]:
                continue

            # BFS 로 팀 찾기
            person = Person((x, y), graph[x][y])
            persons = deque()
            persons.append(person)
            team = Team(persons, 0)
            q = deque()
            q.append((x, y))
            visited[x][y] = True
            three = 0
            while q:
                qx, qy = q.popleft()
                for index in range(4):
                    nx = qx + dx[index]
                    ny = qy + dy[index]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if visited[nx][ny]:
                        continue
                    if graph[nx][ny] == 0 or graph[nx][ny] == 4:
                        continue
                    if graph[nx][ny] == 3:
                        three = Person((nx, ny), graph[nx][ny])
                        continue
                    visited[nx][ny] = True
                    new_person = Person((nx, ny), graph[nx][ny])
                    team.persons.append(new_person)
                    q.append((nx, ny))

            team.persons.append(three)
            team_list.append(team)


def move():
    global team_list

    for index in range(len(team_list)):
        team = team_list[index]
        persons = team.persons  # persons deque
        head = persons.popleft()  # 머리 부터
        hx, hy = head.position
        tail_catch = False
        for index2 in range(4):
            nx = hx + dx[index2]
            ny = hy + dy[index2]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 4:
                graph[nx][ny] = 1
                head.position = (nx, ny)
                graph[hx][hy] = -1  # trace
                persons.append(head)
                break
            elif graph[nx][ny] == 3:  # 꼬리 잡음
                graph[nx][ny] = 1
                head.position = (nx, ny)
                graph[hx][hy] = 3
                persons.append(head)
                tail_catch = True
                break

        while True:
            person = persons.popleft()
            px, py = person.position
            if person.role == 3:  # 꼬리 일 경우
                for index4 in range(4):
                    n3x = px + dx[index4]
                    n3y = py + dy[index4]
                    if n3x < 0 or n3y < 0 or n3x >= n or n3y >= n:
                        continue
                    if graph[n3x][n3y] == -1:  # trace
                        graph[n3x][n3y] = 3
                        person.position = (n3x, n3y)
                        if tail_catch:
                            graph[px][py] = 1
                        else:
                            graph[px][py] = 4  # 이동 칸 처리
                        persons.append(person)
                        break
                break

            # 몸통
            for index3 in range(4):
                n2x = px + dx[index3]
                n2y = py + dy[index3]
                if n2x < 0 or n2y < 0 or n2x >= n or n2y >= n:
                    continue
                if graph[n2x][n2y] == -1:  # trace
                    graph[n2x][n2y] = 2
                    person.position = (n2x, n2y)
                    graph[px][py] = -1  # trace
                    persons.append(person)
                    break

        team_list[index] = team


time = 0


def throw_ball():
    direction = ((time - 1) // n) % 4
    index = (time - 1) % n  # 0 ~ 6
    if direction == 0:
        for y in range(n):
            if graph[index][y] > 0 and graph[index][y] != 4:
                return index, y
    elif direction == 1:
        for x in range(n - 1, -1, -1):
            if graph[x][index] > 0 and graph[x][index] != 4:
                return x, index
    elif direction == 2:
        for y in range(n - 1, -1, -1):
            if graph[index][y] > 0 and graph[index][y] != 4:
                return index, y
    elif direction == 3:
        for x in range(n):
            if graph[x][index] > 0 and graph[x][index] != 4:
                return x, index
    # 만나지 않음
    return None


def get_ball(hx, hy):
    global team_list

    for index in range(len(team_list)):
        team = team_list[index]
        persons = team.persons  # persons deque
        count = 0
        have_mate = False
        while True:
            count += 1
            person = persons.popleft()
            px, py = person.position
            if px == hx and py == hy:
                team.point += (count * count)
                persons.append(person)
                have_mate = True
                while True:
                    temp_person = persons.popleft()
                    if temp_person.role == 1:
                        persons.appendleft(temp_person)
                        break
                    else:
                        persons.append(temp_person)
                break
            if person.role == 3:
                if px != hx or py != hy:
                    persons.append(person)
                    break
            persons.append(person)

        if have_mate:
            persons.reverse()
            temp_tail = persons.popleft()
            temp_tail.role = 1
            tx, ty = temp_tail.position
            graph[tx][ty] = 1
            persons.appendleft(temp_tail)
            temp_head = persons.pop()
            temp_head.role = 3
            htx, hty = temp_head.position
            graph[htx][hty] = 3
            persons.append(temp_head)
            break


find_teams()


for _ in range(k):
    time += 1
    move()
    if throw_ball() is not None:
        hit_x, hit_y = throw_ball()
        get_ball(hit_x, hit_y)

answer = 0

for i in range(len(team_list)):
    temp = team_list[i]
    answer += temp.point
print(answer)
