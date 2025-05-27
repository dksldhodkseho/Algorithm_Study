def solution(arr):
    answer = []
    arr.reverse() #배열 뒤집기
    for i in range(len(arr)):
        num = arr.pop() #마지막 원소를 꺼내어 저장
        if  len(answer) == 0 or num != answer[-1]:
            answer.append(num) # answer배열에 추가
    return answer
