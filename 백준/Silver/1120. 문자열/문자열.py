A,B = input().split()

array =[]
for i in range(len(B)-len(A)+1):
    count = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            count+=1

    array.append(count)

print(min(array))