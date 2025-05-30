def solution(n):
    answer = []
    def hanoi_tower(n,start,end,middle):
        if n == 1:
            answer.append([start,end])
            return
        hanoi_tower(n-1,start,middle,end) # n - 1개의 원판을 1에서 2로 옮기기
        answer.append([start,end]) # n번 원판을 1에서 3으로 옮기기
        hanoi_tower(n-1,middle,end,start) # n - 1개의 원판을 2에서 3으로 옮기기
    hanoi_tower(n,1,3,2)
    return answer
