sticks = list(input())

s = []
total = 0

for i in range(len(sticks)):
    if sticks[i] == '(':
        s.append(sticks[i])
    elif sticks[i] == ')':
        if sticks[i - 1] == '(':
            s.pop()
            total += len(s)
        elif sticks[i - 1] == ')':
            s.pop()
            total += 1

print(total)