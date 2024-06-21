def solution(l, r):
    answer = []
    space = []
    for i in range(l, r+1):
        if i % 5 == 0:
            space.append(i)
            
    for i in space:
        is_exist = True
        
        for j in str(i):
            if j not in ["0","5"]:
                is_exist = False
                break
                
        if is_exist:
            answer.append(i)
            
    if answer:
        return answer
    else:
        return [-1]