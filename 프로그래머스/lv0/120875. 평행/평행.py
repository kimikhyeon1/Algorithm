def solution(dots):
    answer = 0
    first = (dots[0][0]-dots[1][0])/(dots[2][0]-dots[3][0])
    second = (dots[0][1]-dots[1][1])/(dots[2][1]-dots[3][1])
    third = (dots[0][0]-dots[2][0])/(dots[1][0]-dots[3][0])
    four = (dots[0][1]-dots[2][1])/(dots[1][1]-dots[3][1])
    
    
    if first == second or third == four :
        return 1
    return 0