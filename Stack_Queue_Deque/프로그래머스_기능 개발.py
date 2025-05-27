from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    time = deque()
    for i in range(len(progresses)):
        time.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    cnt = 1
    temp = deque()
    temp.append(time.popleft()) #temp에 time의 가장 앞의 원소를 반복하기 전에 미리 꺼내어 저장
    while time:
        comp = time.popleft() #time에서 가장 앞의 원소를 꺼냄
        if comp <= temp[-1]:#꺼낸 원소가 temp의 가장 끝에 원소보다 작다면 temp의 맨 앞에 추가한 뒤 cnt증가 
            temp.appendleft(comp)
            cnt += 1
        else: #꺼낸 원소가 temp의 가장 끝 원소보다 크다면 temp의 맨 끝에 추가한 뒤 cnt를 answer에 저장 그리고 cnt = 1로 초기화
            temp.append(comp)
            answer.append(cnt)
            cnt = 1
    answer.append(cnt) # 마지막에 값 answer 배열에 저장
    return answer
