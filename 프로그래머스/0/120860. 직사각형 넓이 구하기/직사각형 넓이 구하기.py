def solution(dots):
    x1 = dots[0][0]
    y1 = dots[0][1]
    x2, y2 = 0, 0
    
    for i in dots:
        if i[0] != x1:
            x2 = i[0]
        if i[1] != y1:
            y2 = i[1]
                
    x = x1 - x2
    y = y1 - y2
    
    xy = x*y 
    
    if xy < 0:
        xy *= -1
    
    return xy