def solution(numbers):
    answer = 0
    dic = {}
    
    for i in range(10):
        dic[i] = 0
        
    for i in numbers:
        dic[i] += 1
        
    for k,v in dic.items():
        if v == 0:
            answer += k
    return answer