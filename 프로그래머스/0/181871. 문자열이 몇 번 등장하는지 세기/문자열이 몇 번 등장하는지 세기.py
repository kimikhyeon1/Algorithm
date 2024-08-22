def solution(myString, pat):
    answer = 0
    start = 0
    end = len(pat)
    
    while len(myString) >= end:
        if myString[start:end] == pat:
            answer += 1
        start += 1
        end += 1
    return answer