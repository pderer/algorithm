'''
a * x - b(x - 1) >= v
ax - bx + b >= v
x(a - b) >= v - b
x >= (v - b) / (a - b)
'''
import math


a, b, v = map(int, input().split())

diff = a - b
count = 0
height = 0

print(math.ceil((v - b) / (diff)))