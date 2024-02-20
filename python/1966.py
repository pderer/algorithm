from collections import deque


tests = int(input())

for _ in range(tests):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    check = q[m] + 10
    q[m] += 10
    count = 0
    while q:
        if q[0] >= 10:
            q[0] -= 10
            if q[0] < max(q):
                temp = q.popleft()
                q.append(temp + 10)
            else:
                temp = q.popleft()
                count += 1
                if temp + 10 == check:
                    print(count)
                    break
        else:
            b = True
            for i in range(1, len(q)):
                if q[i] >= 10:
                    if q[0] < q[i] - 10:
                        temp = q.popleft()
                        q.append(temp)
                        b = False
                        break
                else:
                    if q[0] < q[i]:
                        temp = q.popleft()
                        q.append(temp)
                        b = False
                        break
            if b:
                q.popleft()
                count += 1