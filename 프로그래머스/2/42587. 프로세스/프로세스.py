from collections import deque



def solution(priorities, location):
    answer = 0
    array = []
    target = priorities[location]
    
    for i in range(len(priorities)):
        array.append([priorities[i],i])
        
    que = deque(array)
    
    while True:
        max_value = max_values(que)
        
        while True:
            if que[0][0] == max_value:
                break
            value = que.popleft()
            que.append(value)
            
        value = que.popleft()
        answer += 1
        if value[1] == location:
            break
    
    return answer

def max_values(array):
    max_value = 0
    for i in array:
        if max_value < i[0]:
            max_value = i[0]
    return max_value