from queue import Queue #큐 라이브러리 사용
q = Queue()

n = int(input())
for i in range(1,n+1):
    q.put(i) # n개의 원소 삽입

while q.qsize() != 1:
    temp = 0
    q.get() #가장 처음 원소 제거
    temp = q.get() #그 뒤의 원소 제거 후 변수에 저장
    q.put(temp) #변수에 저장한 원소 다시 삽입
    
print(q.get()) #마지막 원소 출력
