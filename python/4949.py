while True:
    strings = input()
    if strings == ".":
        break
    stack = []
    for string in strings:
        if string == "(" or string == "[":
            stack.append(string)
        elif string == ")":
            if len(stack) == 0 or stack[-1] != "(":
                print("no")
                break
            else:
                stack.pop()
        elif string == "]":
            if len(stack) == 0 or stack[-1] != "[":
                print("no")
                break
            else:
                stack.pop()
        elif string == ".":
            if len(stack) == 0:
                print("yes")
            else:
                print("no")