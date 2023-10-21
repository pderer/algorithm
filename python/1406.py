from collections import deque
import sys

input = sys.stdin.readline

left = deque(list(input().rstrip()))
right = deque()

m = int(input().rstrip())


for _ in range(m):
    temp = list(input().rstrip().split())
    if temp[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif temp[0] == 'D':
        if right:
            left.append(right.popleft())
    elif temp[0] == 'B':
        if left:
            left.pop()
    elif temp[0] == 'P':
        left.append(temp[1])

result = ''.join(left + right)
print(result)
