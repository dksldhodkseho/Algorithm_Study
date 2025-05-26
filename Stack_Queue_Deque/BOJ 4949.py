while True:
    s = input()
    if s == '.':
        break
    stack = []
    for i in s:
        if i == '(' or i == '[': # 조건1
            stack.append(i)
        elif i == ')': # 조건2
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        elif i == ']': # 조건3
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0: 
        print('yes')
    else:
        print('no')
