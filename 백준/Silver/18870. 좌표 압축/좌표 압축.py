import sys

input = sys.stdin.readline
N = int(input())
array = list(map(int,input().split()))
dic ={}
num_set = set(array)
copy_array = list(num_set)
copy_array.sort()

for i in range(len(copy_array)):
    dic[copy_array[i]] = i
answer = []
for i in range(N):
    answer.append(dic[array[i]])

print(*answer)