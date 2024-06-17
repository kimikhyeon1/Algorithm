def solution(a, d, included):
    answer = 0
    array = []
    for i in range(len(included)):
        array.append(a)
        a += d

    for i in range(len(included)):
        if included[i]:
            answer += array[i]    
    return answer