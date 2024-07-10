def solution(strArr):
    answer = 0
    dic = {}
    for i in strArr:
        if len(i) not in dic:
            dic[len(i)] = 1
        else:
            dic[len(i)] += 1
        
    for k, v in dic.items():
        answer = max(answer,v)
            
    return answer