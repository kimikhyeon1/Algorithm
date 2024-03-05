def solution(n, k):
    answer = 0
    answer +=  (k - n // 10) * 2000 + (n * 12000)  
    return answer