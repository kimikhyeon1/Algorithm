import sys

input = sys.stdin.readline
N = int(input())
array = []
for i in range(N):
    a,b = map(int,input().split())
    array.append([b,a])

array.sort()
for x,y in array:
    print(y,x)