import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
x_num = sorted(list(set(num))) #중복 제거 및 정렬된 배열 생성

dict_num = dict()
for i in range(len(x_num)):
    dict_num[x_num[i]] = i #딕셔너리 업데이트

for i in num:
    print(dict_num[i], end = ' ')
