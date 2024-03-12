def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    start = 0
    end = m
    while end <=len(score):
        price = score[start:end]
        answer += price[-1] * m
        start += m
        end += m
        
    return answer