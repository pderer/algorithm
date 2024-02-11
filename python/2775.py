'''
1층 3호 -> 0층의 1호부터 3호까지 -> 1 + 2 + 3 = 6 : 1 + (2) + (3) = 6 
2층 3호 -> 1층의 1호부터 3호까지 -> 1 + 3 + 6 = 10 : 1 + (1 + 2) + (1 + 2 + 3) = 10
1층 1호 -> 0층의 1호 -> 1
1층 2호 -> 0층의 1호부터 2호까지 -> 1 + 2 = 3
1층 3호 -> 0층의 1호부터 3호까지 -> 6
3층 3호 -> 2층의 1호부터 3호까지 -> 1 + 4 + 10 = 1 + (1 + (1 + 2)) + (1 + (1 + 2) + (1 + 2 + 3)) = 15
2층 1호 -> 1
2층 2호 -> 1 + 3 = 4
2층 3호 -> 10
3층 1호 -> 1
3층 2호 -> 1 + 1 + (1 + 2)
4층 3호 -> 1 + (1 + (1 + (1 + 2))) + (1 + (1 + (1 + 2)) + (1 + (1 + 2) + (1 + 2 + 3)) = 1 + 5 + 15 = 21
1층 4호 -> 1 + 2 + 3 + 4 = 10
2층 4호 -> 1 + (1 + 2) + (1 + 2 + 3) + (1 + 2 + 3 + 4)
3층 4호 -> 1 + (1 + (1 + 2)) + (1 + (1 + 2) + (1 + 2 + 3)) + (1 + (1 + 2) + (1 + 2 + 3) + (1 + 2 + 3 + 4))
4층 4호 -> 1 + (1 + (1 + (1 + 2)) + (1 + (1 + (1 + 2) + (1 + (1 + 2 + (1 + 2 + 3))))
k층 n호 -> (k - 1)층 1호 + (k - 1)층 2호 + ... + (k - 1)층 n호
-> 점화식 -> dynamic programming
'''
t = int(input())
dp = [[0 for _ in range(15)] for _ in range(15)]
for i in range(0, 15):
    dp[0][i] = i + 1

def recursive(k, n):
    if k == 1:
        if dp[k][n] == 0:
            result = 0
            for i in range(1, n + 1):
                result += i
            dp[0][n] = result
        else:
            result = dp[0][n]
        return result
    else:
        if dp[k][n] == 0:
            result = 0
            for i in range(1, n + 1):
                result += recursive(k - 1, i)
            dp[k][n] = result
        else:
            result = dp[k][n]
        return result


for _ in range(t):
    k = int(input())
    n = int(input())
    print(recursive(k, n))
