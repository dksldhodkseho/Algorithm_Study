from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        price = prices.popleft() #첫번째 원소를 뺌
        time = 0
        for i in prices: #뺀 원소를 차례대로 전체와 비교
            time += 1 #시간 체크
            if price > i:
                break
        answer.append(time)
    return answer
