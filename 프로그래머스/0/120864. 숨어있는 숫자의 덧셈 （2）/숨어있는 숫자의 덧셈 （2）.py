def solution(my_string):
    answer = 0
    
    stack = ""
    
    for i in my_string:
        if 47 < ord(i) < 59:
            stack += i
        elif len(stack) > 0:
            answer += int(stack)
            stack = ""
    
    if stack:
        answer += int(stack)
    return answer