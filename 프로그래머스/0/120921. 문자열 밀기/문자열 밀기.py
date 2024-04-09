def solution(A, B):
    answer = 0
    for i in range(len(A)):
        if A == B:
            return answer
        temp = A[-1]
        A = temp + A[:-1]
        answer += 1
         
    return -1