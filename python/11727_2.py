n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3

def tile(t):
    if t == 1 or t == 2:
        return dp[t]
    if dp[t] != 0 and dp[t - 2] != 0:
        dp[t] = dp[t - 1] + 2 * dp[t - 2]
        return dp[t]
    else:  
        new_tile = tile(t - 1) + 2 * tile(t - 2)
    return new_tile

print(tile(n) % 10007)