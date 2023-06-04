N, M = map(int,input().split())

array_A = list(map(int,input().split()))
array_B = list(map(int,input().split()))

answer = []

A_point = 0
B_point = 0

while A_point <= len(array_A)-1 or B_point <= len(array_B)-1:
    if A_point == len(array_A):
        answer.append(array_B[B_point])
        B_point+=1
        continue
    elif B_point == len(array_B):
        answer.append(array_A[A_point])
        A_point +=1
        continue

    if array_A[A_point] <= array_B[B_point]:
        answer.append(array_A[A_point])
        A_point +=1
    else:
        answer.append(array_B[B_point])
        B_point += 1

print(*answer)
