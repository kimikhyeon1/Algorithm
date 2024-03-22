def solution(order):
    answer = 0
    for i in range(len(str(order))):
        if str(order)[i] in ["3","6","9"]:
            answer += 1
    return answer