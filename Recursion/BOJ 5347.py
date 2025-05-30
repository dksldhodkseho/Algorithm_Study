import sys
input = sys.stdin.readline

def gcd(a, b): #최대공약수 구하는 함수
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())
result = []
for i in range(n):
    num1, num2 = map(int, input().split())
    lcm = (num1 * num2) // gcd(num1,num2) 
    result.append(lcm)
for i in result:
    print(i)
