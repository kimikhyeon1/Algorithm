def solution(sides):
    answer = 1
    sides.sort()
    if sides[-1] >= sides[0] + sides[1]:
        return 2
    return answer