import heapq
import sys


n = int(sys.stdin.readline())

heap = []

for _ in range(n):
    temp = int(sys.stdin.readline())
    if temp == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, temp)
