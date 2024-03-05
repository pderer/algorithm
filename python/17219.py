from sys import stdin


input = stdin.readline
n, m = map(int, input().split())

site = {}

for _ in range(n):
    k, v = map(str, input().split())
    site[k] = v

for _ in range(m):
    print(site[input().rstrip()])