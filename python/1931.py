n = int(input())

meeting = []

for _ in range(n):
    meeting.append(tuple(map(int, input().split())))

meeting.sort(key = lambda x: (x[1], x[0]))

answer = 1
start, end = meeting[0]

for i in range(1, n):
    temp_start, temp_end = meeting[i]
    if end <= temp_start:
        start = temp_start
        end = temp_end
        answer += 1

print(answer)