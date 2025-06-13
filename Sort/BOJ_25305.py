import sys
input = sys.stdin.readline

n, k = map(int, input().split())
score = list(map(int,input().split()))
score.sort(reverse = True) #배열 내림차순 정렬
print(score[k-1]) #k-1원소 출력
