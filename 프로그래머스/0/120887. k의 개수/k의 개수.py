def solution(i, j, k):
    answer = 0
    for v in range(i,j + 1):
        for ch in str(v):
            if str(k) == ch:
                answer += 1
    return answer