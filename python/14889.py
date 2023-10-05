from itertools import combinations, permutations


n = int(input())
data = []
index = []
INF = 999999999

for i in range(n):
    data.append(list(map(int, input().split())))
    index.append(i)

combination_list = list(combinations(index, int(n / 2)))

# print(combination_list)
start_score = []
link_score = []
for i in range(int(len(combination_list) / 2)):
    j = len(combination_list) - 1 - i
    start_perm_list = list(permutations(combination_list[i], 2))
    link_perm_list = list(permutations(combination_list[j], 2))
    # print(start_perm_list)
    # print()
    # print(link_perm_list)
    temp_start = 0
    temp_link = 0
    for start in start_perm_list:
        temp_start += data[start[0]][start[1]]
    for link in link_perm_list:
        temp_link += data[link[0]][link[1]]

    start_score.append(temp_start)
    link_score.append(temp_link)

minimum = INF
for i in range(len(start_score)):
    if minimum > abs(start_score[i] - link_score[i]):
        minimum = abs(start_score[i] - link_score[i])

# print(start_score)
# print(link_score)
print(minimum)