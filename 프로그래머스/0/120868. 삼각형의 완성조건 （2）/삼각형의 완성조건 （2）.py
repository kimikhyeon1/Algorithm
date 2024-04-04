def solution(sides):
    sides.sort()
    min_num = sides[1] - sides[0]
    max_num = sides[1] + sides[0]
    answer = max_num - min_num -1
        
    return answer