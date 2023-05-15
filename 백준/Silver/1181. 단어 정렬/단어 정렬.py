import sys

input = sys.stdin.readline
N = int(input())
array = []

for i in range(N):
    ch = input().strip()
    array.append(ch)

array.sort()
array.sort(key = lambda x:len(x))
double = ""
for i in array:
    if i==double:
        continue
    double=i
    print(i)