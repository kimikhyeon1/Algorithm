def solution(s):
    answer = True
    
    array = []
    for i in s:
        if i == "(":
            array.append(i)
        elif i == ")":
            if not array:
                return False
            else:
                array.pop()

    if array:
        return False
    return True