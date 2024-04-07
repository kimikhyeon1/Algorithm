def solution(n, k):
    answer = []
    a = 1
    while n >= a * k:
        answer.append(a * k)
        a += 1

    return answer