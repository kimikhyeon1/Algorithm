import sys
input = sys.stdin.readline
m,n = map(int,input().split())
array = list(map(int,input().split()))
array_sum = [array[0]]
for i in range(1,len(array)):
    array_sum.append(array_sum[-1]+array[i])

for i in range(n):
    first,second = map(int,input().split())
    if first == 1:
        print(array_sum[second-1])
    else:
        print(array_sum[second-1] - array_sum[first-2])