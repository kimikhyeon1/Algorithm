def solution(n):
    temp = str(n)
    answer = 0
    for i in range(len(temp)):
        answer += int(temp[i])
    return answer