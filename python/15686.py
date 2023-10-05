from itertools import combinations

INF = 999999999

n, m = map(int, input().split())

chicken_list = [] # 치킨집 리스트 [(x,y)]
home_list = []
chicken_distance = []

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 2:
            chicken_list.append((i + 1, j + 1))
        elif temp[j] == 1:
            home_list.append((i + 1, j + 1))

chosen_list = list(combinations(chicken_list, m))

for i in range(len(chosen_list)):
    distance = 0
    for home in home_list:
        minimum = INF
        for chosen in chosen_list[i]:
            if minimum > abs(home[0] - chosen[0]) + abs(home[1] - chosen[1]):
                minimum = abs(home[0] - chosen[0]) + abs(home[1] - chosen[1])
        distance += minimum
    chicken_distance.append(distance)
            
print(min(chicken_distance))