import sys
input = sys.stdin.readline

N, M = map(int,input().split())
array = []
for i in range(N):
    array.append(int(input()))

array.sort()

answer = 100000000000000

start = 0
end = 0

while len(array) > end and len(array) > start:
    num = array[end] - array[start]
    
    if num >= M:
        answer = min(answer,num)
        start+=1
    else:
        end+=1
    
    
print(answer)
