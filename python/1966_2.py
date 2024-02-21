from collections import deque


tests = int(input())

for _ in range(tests):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    count = 0
    while q:
        m -= 1
        if q[0] < max(q):
            temp = q.popleft()
            q.append(temp)
        else:
            q.popleft()
            count += 1
            if m < 0:
                print(count)
                break
        if m < 0:
            m = len(q) - 1