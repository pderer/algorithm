n, m, k = map(int, input().split())

guns = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] > 0:
            guns[i][j].append(temp[j])


class Player:
    def __init__(self, point, d, power, number):
        self.point = point
        self.d = d
        self.power = power
        self.gun = 0  # 총 잡으면 생김
        self.number = number


players = [-1]  # index 0은 쓰레기 값
for i in range(1, m + 1):
    temp = list(map(int, input().split()))
    temp[0] -= 1
    temp[1] -= 1
    players.append(Player((temp[0], temp[1]), temp[2], temp[3], i))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

points = [-1] + [0] * m


def move():
    for index in range(1, m + 1):
        player = players[index]
        px, py = player.point
        pd = player.d
        nx = px + dx[pd]
        ny = py + dy[pd]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            if pd == 0:
                pd = 2
            elif pd == 1:
                pd = 3
            elif pd == 2:
                pd = 0
            elif pd == 3:
                pd = 1
            nx = px + dx[pd]
            ny = py + dy[pd]

        player.point = (nx, ny)
        player.d = pd

        # 플레이어 있는지 확인
        winner = 0
        loser = 0
        for index2 in range(1, m + 1):

            if index == index2:
                continue
            player2 = players[index2]
            p2x, p2y = player2.point
            p2total = player2.power + player2.gun
            p1total = player.power + player.gun

            if nx == p2x and ny == p2y: # 싸운다.
                if p1total > p2total:
                    points[index] += (p1total - p2total)
                    winner = player
                    loser = player2
                elif p2total > p1total:
                    points[index2] += (p2total - p1total)
                    winner = player2
                    loser = player
                else:
                    if player.power > player2.power:
                        winner = player
                        loser = player2
                    else:
                        winner = player2
                        loser = player
            else:
                continue

        # 싸웠으니 정산
        if winner != 0:
            # 패자
            lx, ly = loser.point
            ld = loser.d
            ln = loser.number
            lg = loser.gun
            if lg != 0: # 총을 갖지 않은 경우, append 할 필요 없음
                guns[lx][ly].append(lg)
            loser.gun = 0

            is_other = False

            for index4 in range(4):
                l2x = lx + dx[ld]
                l2y = ly + dy[ld]
                for index3 in range(1, m + 1): # range 작성안했음
                    if index3 == ln:
                        continue
                    temp_player = players[index3]
                    tx, ty = temp_player.point
                    if l2x == tx and l2y == ty:
                        is_other = True
                if l2x < 0 or l2y < 0 or l2x >= n or l2y >= n or is_other:
                    ld += 1
                    if ld > 3:
                        ld = 0
                    is_other = False  # 플레이어가 있어서 방향을 바꾼 경우, 다시 False로 해줘야 함  # noqa: E501
                else:
                    loser.point = (l2x, l2y)
                    loser.d = ld
                    break

            # 패자가 이동했는데 총이 있으면
            l2tx, l2ty = loser.point
            if len(guns[l2tx][l2ty]) > 0:
                guns_list = guns[l2tx][l2ty]
                temp_gun = max(guns_list)
                loser.gun = temp_gun
                guns[l2tx][l2ty].remove(temp_gun)

            # 승자
            wx, wy = winner.point
            if len(guns[wx][wy]) > 0:
                # 가진 총이 없을 때
                if winner.gun == 0:
                    # 총을 가짐
                    max_gun = max(guns[wx][wy])
                    winner.gun = max_gun
                    guns[wx][wy].remove(max_gun)
                # 가진 총이 있음
                else:
                    guns_list = guns[wx][wy]
                    temp_gun = max(guns_list)
                    # 떨어진 총이 더 공격력이 큼
                    if winner.gun < temp_gun:
                        guns[wx][wy].append(winner.gun)
                        winner.gun = temp_gun
                        guns[wx][wy].remove(temp_gun)

        # 플레이어 없어서 안싸움, 총 확인
        else:
            if len(guns[nx][ny]) > 0:
                # 가진 총이 없을 때
                if player.gun == 0:
                    # 총을 가짐
                    max_gun = max(guns[nx][ny])
                    player.gun = max_gun
                    guns[nx][ny].remove(max_gun)
                # 가진 총이 있음
                else:
                    guns_list = guns[nx][ny]
                    temp_gun = max(guns_list)
                    if player.gun < temp_gun:
                        guns[nx][ny].append(player.gun)
                        player.gun = temp_gun
                        guns[nx][ny].remove(temp_gun) # 복붙하느라 신경 안썼음


# k 라운드
for _ in range(k):
    move()

for i in range(1, len(points)):
    print(points[i], end=" ")