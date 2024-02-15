'''
가장 적은 봉지를 들고 가려 한다. -> 가장 많은, 큰, 작은, 적은 -> 그리디 의심
바로 문제 유형이 안떠오르면 그리디일 가능성 높음
그리디로 안되면 DP, 그래프 알고리즘 의심
'''
n = int(input())
bags = 0

while n > 0:
    if n % 5 == 0:
        bags += n / 5
        n = 0
    else:
        n -= 3
        bags += 1
if n < 0:
    print(-1)
else:
    print(int(bags))