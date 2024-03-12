def solution(t, p):
    answer = 0
    start =0
    end = len(p)
    while end <= len(t):
        if int(p) >= int(t[start:end]):
            answer += 1
        start += 1
        end += 1            
        
    return answer