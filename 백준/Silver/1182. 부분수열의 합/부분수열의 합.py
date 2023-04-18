import sys
input = sys.stdin.readline

N,M = map(int,input().split())
array = list(map(int,input().split()))
answer = 0
sum_array = []

def SUM(number):
    global answer

    if M == sum(sum_array) and len(sum_array)>0:
        answer+=1

    for i in range(number,N):
        sum_array.append(array[i])
        SUM(i+1)
        sum_array.pop()

SUM(0)
print(answer)