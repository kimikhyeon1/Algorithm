import sys

input = sys.stdin.readline
N = int(input())
array = []

for i in range(N):
    age, name = input().split()
    array.append([int(age),i,name])

array.sort()

for k,index,v in array:
    print(k,v)