import sys
input = sys.stdin.readline

n = int(input())
word = []

for i in range(n):
    word.append(input().rstrip()) #입력받은 단어를 배열에 추가

word = list(set(word)) #중복 제거
word = sorted(word, key = lambda x: (len(x), x)) #조건에 맞게 정렬

for i in word:
    print(i)
