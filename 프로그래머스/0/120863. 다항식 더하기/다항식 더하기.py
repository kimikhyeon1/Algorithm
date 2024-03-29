def solution(polynomial):
    answer = ''
    x = 0
    number = 0
    
    for i in range(len(polynomial)):
        if polynomial[i] == 'x':
            if i == 0 or polynomial[i - 1] == " ":
                x += 1
            else:
                x += int(polynomial[i - 1])
            continue
        
        if 48 < ord(polynomial[i]) < 65:
            if i == len(polynomial) - 1:
                number += int(polynomial[i])
            elif polynomial[i + 1] != 'x':
                number += int(polynomial[i])
    
    if x == 1:
        answer = 'x'
    if x > 1:
        answer = str(x) + 'x'
    
    if number > 0:
        if len(answer) > 0:
            answer += " + " + str(number)
        else:
            answer = str(number)
                
    return answer