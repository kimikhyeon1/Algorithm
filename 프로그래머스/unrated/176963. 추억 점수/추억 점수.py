def solution(name, yearning, photo):
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
        
    answer = []
    
    for i in photo:
        csum = 0
        for j in i:
            if j in dic:
                csum+=dic[j]
        answer.append(csum)

    return answer