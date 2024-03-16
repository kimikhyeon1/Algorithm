from collections import deque

def solution(num_list, n):
    answer = []
    count = 0
    array = []
    que = deque(num_list)
    while que:
        array.append(que.popleft())
        count += 1 
        if count == n:
            count = 0
            answer.append(array)
            array = []
    
    return answer