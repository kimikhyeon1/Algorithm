N,M = map(int,input().split())
array = [i for i in range(1,N+1)]

for ball in range(M):
    i,j = map(int,input().split())
    array[i-1:j] = reversed(array[i-1:j])

print(*array)

