def solution(n):
    answer = 1
    pizza = 6
    while True:
        if pizza % n == 0:
            return answer
        answer += 1
        pizza += 6
    return answer