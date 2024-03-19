def solution(my_string):
    answer = ''
    for ch in my_string:
        if 65 <= ord(ch) <= 90:
            answer += chr(ord(ch) + 32)
        else:
            answer += chr(ord(ch) - 32)
    
    return answer