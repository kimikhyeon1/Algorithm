def solution(polynomial):
    number = 0
    x = 0
    stack = list(polynomial)
    number_space = ""
    is_x = False
    while stack:
        temp = stack.pop()
        
        if temp == " ":
            if is_x:
                if number_space:
                    x += int(number_space[::-1])
                else:
                    x += 1
                is_x = False
            else:
                if number_space:
                    number += int(number_space[::-1])
            number_space = ""
            
        if temp == "x":
            is_x = True
        
        if 45 < ord(temp) < 65:
            number_space += temp
    
    if is_x:
        if number_space:
            x += int(number_space[::-1])
        else:
            x += 1
    elif number_space:
        number += int(number_space[::-1])
            
    answer = ""
    
    if x == 1:
        answer += "x"
    elif x > 1:
        answer += str(x)+"x"
    
    if number > 0:
        if x:
            answer += " + " + str(number)
        else:
            answer += str(number)
            
    return answer