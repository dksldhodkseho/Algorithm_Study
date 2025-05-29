def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(': #'('라면 스택에 저장
            stack.append(i)
        elif i == ')' and len(stack) == 0: #')'이고 스택의 길이가 0이라면 스택에 저장
            stack.append(i)
        elif i == ')' and stack[-1] == '(': #')'이고 스택의 마지막 원소가 '('라면 pop()을 통해 스택의 마지막 원소를 빼줌
            stack.pop()
        if len(stack) == 0:
            answer = True
        else:
            answer = False
    return answer
