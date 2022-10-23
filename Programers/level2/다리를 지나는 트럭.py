def solution(bridge_length, weight, truck_weights):
    time = 0
    truckOnBridge = [0] * bridge_length
    while truckOnBridge:
        time += 1
        truckOnBridge.pop(0)
        if truck_weights:
            if sum(truckOnBridge) + truck_weights[0] <= weight:
                truckOnBridge.append(truck_weights.pop(0))
            else:
                truckOnBridge.append(0)
    return time


print(solution(2, 10, [7, 4, 5, 6]))