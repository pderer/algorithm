import sys
input = sys.stdin.readline # 개행문자 (\n) 도 받으므로 rstrip()을 호출

t = int(input().rstrip())
for _ in range(t):
    scores = []
    success = 1
    n = int(input().rstrip())
    for _ in range(n):
        scores.append(tuple(map(int, input().rstrip().split())))
    scores.sort()
    first_paper, first_interview = scores[0]
    for i in range(1, n):
        paper, interview = scores[i]
        if interview < first_interview:
            success += 1
            first_interview = interview
    print(success)