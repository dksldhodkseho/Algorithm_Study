from collections import deque
def solution(priorities, location):
    answer = 1
    temp = []
    dq = deque(enumerate(priorities)) #enumerate()를 통해 튜플 형태로 저장
    while dq:
        pro = dq.popleft() #앞에서부터 차례대로 원소 꺼내기
        cnt = 0
        for i in dq:
            if pro[1] < i[1]: #우선순위가 더 높은게 있다면 다시 deque에 저장
                dq.append(pro)
                break
            else:
                cnt += 1
        if cnt == len(dq): #우선순위가 더 높은게 없다면 temp에 저장
            temp.append(pro)
        
    for i in temp: #temp배열에서 i[0] == location인 값 찾기
        if i[0] == location:
            break
        answer += 1
    
    return answer
