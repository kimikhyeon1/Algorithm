def solution(n):
    real = n
    answer = []
    
    while True:
        is_find = False
        for i in range(2,n + 1):           
            if n % i == 0:
                n = n // i
                if i not in answer:
                    answer.append(i)
                is_find = True
                break
        
        if n == real:
            retunr [n]
        if is_find == False:
            break
                    
    return answer