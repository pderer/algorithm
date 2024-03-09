'''
작은 문제를 풀어서 큰 문제를 해결할 수 있다
작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다
-> DP
점화식 구하기
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = stairs[1] + stairs[3] OR stairs[2] + stairs[3]
dp[4] = stairs[1] + stairs[2] + stair[4] OR stairs[1] + stairs[3] + stairs[4]

규칙성 찾기
dp[n] = dp[n - 2] + stairs[n] OR dp[n - 3] + stairs[n - 1] + stairs[n]
'''

n = int(input())
stairs = [0] * 301

for i in range(1, n + 1):
    stairs[i] = int(input())

dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n])