import sys
input = sys.stdin.readline

n = int(input())

dot = [] 
for i in range(n):
    x, y = map(int, input().split())
    dot.append([x,y])# 입력 받은 좌표값을 배열에 저장

dot = sorted(dot, key = lambda x: (x[1], x[0])) #조건에 맞게 정렬

for i in dot:
    print(i[0], i[1])
