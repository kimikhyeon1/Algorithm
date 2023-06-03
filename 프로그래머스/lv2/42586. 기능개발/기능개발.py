from collections import deque
def solution(progresses, speeds):
    answer = []
    
    point = 0
        
    while point < len(speeds):
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
            
        count = 0
        
        while point < len(speeds):
            if progresses[point] >= 100:
                count +=1
                point +=1
            else:
                break
        
        if count > 0:
            answer.append(count)
        
    return answer