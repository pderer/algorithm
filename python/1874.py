n = int(input())

stack = []
print_stack = []
first = int(input())
for i in range(1, first + 1):
    stack.append(i)
    print_stack.append("+")

stack.pop()
print_stack.append("-")
current = first + 1
result = True

for _ in range(n - 1):
    check = False
    # print('-------')
    num = int(input())
    # print(f"num: {num}")
    while stack and stack[-1] >= num:
        temp = stack.pop()
        if num == temp:
            print_stack.append("-")
            check = True
            break
    for i in range(current, num + 1):
        stack.append(i)
        print_stack.append("+")
        current = num + 1
    while stack and stack[-1] >= num:
        temp = stack.pop()
        if num == temp:
            print_stack.append("-")
            check = True
            break
    # print(stack)
    if check is False:
        result = False

if result:
    for sign in print_stack:
        print(sign)
else:
    print("NO")