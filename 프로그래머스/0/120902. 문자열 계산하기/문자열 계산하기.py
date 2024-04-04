from collections import deque
def solution(my_string):
    def is_int(i):
        if 47 < ord(i) < 58:
            return True
        return False
    
    que = deque()
    number = ""
    for i in my_string:
        if is_int(i):
            number += i
        
        if i == "+" or i == "-":
            que.append(int(number))
            number = ""
    
    if number != "":
        que.append(int(number))
        
    answer = que.popleft()
    
    for i in my_string:
        if i == "+" or i == "-":
            number = que.popleft()

            if i == "+":
                answer += number
            else:
                answer -= number  
                   
    return answer