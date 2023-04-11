import sys

input = sys.stdin.readline
n, k = map(int, input().split())
array = list(map(int, input().split()))

array_sum = sum(array[:k])

Max_sum = array_sum

for i in range(k,n):
    array_sum += array[i] - array[i-k]

    if array_sum > Max_sum:
        Max_sum = array_sum

print(Max_sum)