def solution(code):
    answer = ''
    mode = False
    for i in range(len(code)):
        if code[i] == '1':
            mode = not mode
            continue
            
        if mode == False and i % 2 == 0:
            answer += code[i]
        elif mode == True and i % 2 != 0:
            answer += code[i]
    if answer == "":
        return "EMPTY"
    return answer