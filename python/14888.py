n = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -1e9
min_value = 1e9

# DFS를 사용하는 이유 : 그 전 값을 가지고 연산을 해야 함 -> 재귀
def dfs(i, now): # i: index, now: 누적된 연산 값
    global max_value, min_value, add, sub, mul, div
    if i == n: # 계산을 다 했을 때, 최대 최소 업데이트
        max_value = max(max_value, now)
        min_value = min(min_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + num_list[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - num_list[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * num_list[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / num_list[i]))
            div += 1

dfs(1, num_list[0])
print(max_value)
print(min_value)