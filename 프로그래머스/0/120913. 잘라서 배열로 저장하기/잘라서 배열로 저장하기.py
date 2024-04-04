def solution(my_str, n):
    array = []
    start = 0
    end = n
    for i in range(len(my_str) // n):
        array.append(my_str[start:end])
        start += n
        end += n
    
    if len(my_str) % n != 0:
        array.append(my_str[start:])
    return array