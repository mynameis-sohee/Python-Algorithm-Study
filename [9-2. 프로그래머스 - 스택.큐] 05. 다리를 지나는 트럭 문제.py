from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    bridge_weight = 0
    while bridge:
        answer += 1
        bridge.popleft()
        if truck_weights:
            if bridge_weight+truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0) 
    return answer


print(solution(2,10,[7,4,5,6]))
