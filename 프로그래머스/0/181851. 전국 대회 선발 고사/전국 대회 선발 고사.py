def solution(rank, attendance):
    answer = 0
    dic = {}
    for i, k in enumerate(rank):
        if attendance[i]:
            dic[k] = i
    
    sort_dic = sorted(dic)
    answer = dic[sort_dic[0]] * 10000 + dic[sort_dic[1]] * 100 + dic[sort_dic[2]]
    return answer