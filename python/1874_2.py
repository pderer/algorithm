n = int(input())

current = 1
stack = []
print_stack = []
check = True
for _ in range(n):
    num = int(input())
    while current <= num:
        stack.append(current)
        print_stack.append("+")
        current += 1
    
    if stack[-1] == num:
        stack.pop()
        print_stack.append("-")
    else:
        check = False
        break

if check:
    for sign in print_stack:
        print(sign)
else:
    print("NO")
    