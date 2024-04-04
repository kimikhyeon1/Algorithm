def solution(balls, share):
    factorial = [1 for _ in range(balls + 1)]
    
    for i in range(1,balls + 1):
        factorial[i] = factorial[i - 1] * i 
    
    answer = factorial[balls] // (factorial[balls - share] * factorial[share])
    
    return answer
    