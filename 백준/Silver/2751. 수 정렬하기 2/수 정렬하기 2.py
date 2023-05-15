import sys

input = sys.stdin.readline
N = int(input())
array=[]
for i in range(N):
    x = int(input())
    array.append(x)

array.sort()
for i in array:

    print(i)