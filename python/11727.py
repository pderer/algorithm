'''
n = 1 -> 1
n = 2 -> 3
n = 3 -> 5
n = 4 -> 11
n = 5 -> 21
n = 6 -> 43
n = 7 -> 85
n = 8 -> 171
'''

n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]

print(dp[n] % 10007)