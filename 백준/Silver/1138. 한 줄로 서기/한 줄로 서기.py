import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))
answer = [0]*n

for i in range(n):
    count = 0
    for j in range(n):
        if array[i] ==count and answer[j]==0:
            answer[j]=i+1
            break
        elif answer[j]==0:
            count+=1

print(*answer)