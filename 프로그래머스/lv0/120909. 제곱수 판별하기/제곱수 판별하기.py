def solution(n):
    answer = 1
    double =0
    while answer < n:
        double = answer*answer
        answer += 1
        if double == n:
            return 1
    return 2