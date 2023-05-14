N,M = map(int,input().split())
array = [0]*N

for ball in range(M):
    i,j,k = map(int,input().split())
    for x in range(i-1,j):
        array[x]=k

print(*array)
