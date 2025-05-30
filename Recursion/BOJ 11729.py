n = int(input()) 
def hanoi_tower(n,start,end,middle): # n = 옮길 원판의 개수 start = 시작위치, end = 도착 위치, middle = 보조 위치
    if n == 1:
        print(start,end)
        return
    
    hanoi_tower(n-1,start,middle,end) # n-1개의 원판을 start에서 middle로 옮기기
    print(start,end) # n을 start에서 end로 옮기기
    hanoi_tower(n-1,middle,end,start) # n-1개의 원판을 middle에서 end로 옮기기
    
print(2**n - 1) # 하노이 탑의 이동 횟수
hanoi_tower(n,1,3,2)
