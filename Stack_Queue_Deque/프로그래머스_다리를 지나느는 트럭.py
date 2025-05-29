from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    cur_weight = 0
    
    while len(truck_weights) > 0:
        time += 1 #시간을 계속해서 더해줌
        cur_weight = cur_weight - bridge.popleft() #시간이 흐를 때마다 bridge에서 하나씩 빼줌
        if cur_weight + truck_weights[0] <= weight: #트럭이 올라올 수 있다면 현재무게에 트럭무게를 더해주고 bridge에 추가해줌
            cur_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0) #조건을 만족 못한다면 0을 삽입함
    answer = time + bridge_length #마지막 원소가 들어왔을 때의 시간 + 다리의 길이
    return answer
