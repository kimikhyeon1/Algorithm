from collections import deque
def solution(order):
    answer = 0
    assist_belt = []
    main_belt = deque([i for i in range(1, len(order) + 1)])
    
    pointer = 0
    while main_belt:
        if main_belt[0] == order[pointer]:
            pointer += 1
            answer += 1
            main_belt.popleft()
            continue
        else:
            if assist_belt:
                if assist_belt[-1] == order[pointer]:
                    assist_belt.pop()
                    pointer += 1
                    answer += 1
                    continue
            assist_belt.append(main_belt.popleft())
    
    while assist_belt:
        if assist_belt[-1] == order[pointer]:
            assist_belt.pop()
            pointer += 1
            answer += 1
        else:
            break

                    
    return answer