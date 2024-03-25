def solution(array, n):
    answer = 0
    index = 0
    
    if n in array:
        return n
    
    array.append(n)
    array.sort()
    
    for i in range(len(array)):
        if array[i] == n:
            index = i
            
    if index == 0:
        return array[1]
    if index == len(array) - 1:
        return array[-2]
    
    if array[index + 1] - n == n - array[index - 1]:
        answer = array[index - 1]
    elif array[index + 1] - n > n - array[index - 1]:
        answer = array[index - 1]
    else:
        answer = array[index + 1]
            
    return answer