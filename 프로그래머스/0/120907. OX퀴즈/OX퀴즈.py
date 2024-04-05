from collections import deque
def solution(quiz):
    answer = []
    
    number = deque()
    
    for i in quiz:
        num = ""
        for j in i :
            if 42 < ord(j) < 58:
                num += j
            
            if j == " " and num != "":
                number.append(num)
                num = ""
        
        number.append(num)
    
    while number:
        x = number.popleft()
        formula = number.popleft()
        y = number.popleft()
        ans = number.popleft()
        xy = 0
        
        if x[0] == "-":
            x = int(x[1:]) * -1
        else:
            x = int(x)
            
        if y[0] == "-":
            y = int(y[1:]) * -1
        else:
            y = int(y)
        
        if formula == "+":
            xy = x + y
        
        else:
            xy = x - y
            
        if ans[0] == "-":
            ans = int(ans[1:]) * -1
        else:
            ans = int(ans)
        
        if ans == xy:
            answer.append("O")
        else:
            answer.append("X")
        
    return answer