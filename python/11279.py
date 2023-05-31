import heapq
import sys
hq = []

n = int(sys.stdin.readline())
for _ in range(n):
    command = int(sys.stdin.readline())
    if command == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(hq))
    else:
        heapq.heappush(hq, -1 * command)
