import sys

input = sys.stdin.readline

N = int(input())

array = [0] *(N+1)
array[0], array[1] = 1,2

for i in range(2,N):
    array[i] = array[i-2]+array[i-1]

print(array[N-1]%10007)