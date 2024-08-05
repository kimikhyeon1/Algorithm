def solution(x, n):
    answer = []
    start = 0
    for i in range(n):
        start += x
        answer.append(start)
    return answer