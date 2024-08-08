def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    answer = []
    min_number = min(arr)
    
    for i in arr:
        if i == min_number:
            continue
        answer.append(i)
        
    return answer