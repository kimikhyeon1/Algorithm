def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if arr[i] == 2:
            answer.append(i)
            break
    
    if len(answer) == 0:
        return [-1]
    
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 2:
            if answer[0] == i:
                return [2]
            else:
                answer.append(i)
                break
    
    return arr[answer[0]:answer[1] + 1]