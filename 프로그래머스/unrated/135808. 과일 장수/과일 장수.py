def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    min = 0
    max = m
    while True:
        if max >len(score):
            return answer
        space = score[min:max]
        min+=m
        max+=m
        answer+= space[-1]*m