def solution(my_string):
    answer = ''
    array = ["a","e","i","o","u"]
    for i in my_string:
        if i in array:
            continue
        answer += i 
    return answer