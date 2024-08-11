def solution(s):
    answer = ''
    count = 0
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
            count = 0
            continue
            
        if count % 2 != 0:
            answer += s[i].lower()
        else:
            answer += s[i].upper()
    
        count += 1
    return answer