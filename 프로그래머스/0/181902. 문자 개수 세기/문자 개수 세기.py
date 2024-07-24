def solution(my_string):
    answer =  [0] * 52
    
    for ch in my_string:
        if ord(ch) < 91:
            index = ord(ch) - 65
        else:
            index = ord(ch) - 71
        answer[index] += 1

    return answer