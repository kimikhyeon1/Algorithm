# 1. 다리에 대기중인 트럭(다리 트럭)과 대기 트럭을 que구조로 저장한다.
# 2. 대기 트럭이 존재하지 않을때 까지 while문을 진행한다.
#   - 다리 트럭 값의 무게를 저장할 sum_bridge 변수를 생성한다. (SUM을 이용하면 시간초과 이슈)
#   - 다리 트럭의 맨 앞 값은 다리를 지나야 하기 때문에 pop을 진행
#       - 만약 pop한 값이 0보다 크면 sum_bridge에서 나간 트럭 값을 빼준다.
#   - sum_bridge의 값과 대기 트럭 첫번째 트럭의 합친 값이 weigh보다 작거나 같다면 트럭을 다리로 이동한다.
#       - 그렇지 않다면 다리 트럭에 0을 추가해 배열 길이를 맞춰준다.
#   - time 변수에 1초를 추가한다.
# 3. while문이 종료 후 다리를 지나고 있는 트럭이 모두 다리를 건널 수 있게 while문을 진행한다.

from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])     
    sum_bridge = 0
    time = 0
    
    while truck_weights:
        out_truck = bridge.popleft()
        if out_truck > 0:
            sum_bridge -= out_truck
            
        if truck_weights[0] + sum_bridge <= weight:
            truck = truck_weights.popleft()
            sum_bridge += truck
            bridge.append(truck)
        else:
            bridge.append(0)
        
        time += 1
    
    while sum_bridge:
        out_truck = bridge.popleft()
        if out_truck > 0:
            sum_bridge -= out_truck
        time += 1
    
    return time