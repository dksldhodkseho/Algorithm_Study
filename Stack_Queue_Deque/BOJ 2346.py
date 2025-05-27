from collections import deque

n = int(input()) 
dq = deque(enumerate(map(int,input().split()))) #enumerate를 사용하여 튜플 형태로 deque에 저장
result = []

while dq: #dq가 빌때까지 반복
    balloon, paper = dq.popleft() # 튜플 형태 이므로 첫번 째 풍선과 종이에 써져 있는 숫자가 각각 변수에 저장
    result.append(balloon + 1) #풍선 번호 배열에 저장
    
    if paper > 0:
        dq.rotate(-(paper - 1))# 숫자가 양수라면 반시계 숫자 - 1만큼 반시계 방향으로 돌림
    elif paper < 0: 
        dq.rotate(-paper) #숫자가 음수라면 숫자 만큼 시계 방향으로 돌림
        
for i in result:
    print(i, end = ' ')
