strings = list(input())

bomb = list(input())

s = []

for i in range(len(strings)):
    s.append(strings[i])
    if s[-1] == bomb[-1]:
        if len(s) >= len(bomb):
            if s[-len(bomb):] == bomb:
                for j in range(len(bomb)):
                    s.pop()

if s:
    print(''.join(s))
else:
    print('FRULA')