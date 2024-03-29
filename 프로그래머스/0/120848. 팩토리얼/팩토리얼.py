def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

def solution(n):
    answer = 0
    count = 0
    while answer <= n:
        count += 1
        answer = factorial(count)
    return count - 1