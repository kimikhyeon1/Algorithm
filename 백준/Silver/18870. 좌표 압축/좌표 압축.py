import sys

input = sys.stdin.readline
N = int(input())
array = list(map(int,input().split()))
dic ={}
copy_array = array[:]
copy_array.sort()
double = 0
count = 0
answer = []

for i in range(N):
    if double == copy_array[i]:
        continue
    double= copy_array[i]
    dic[copy_array[i]] = count
    count+=1

for i in range(N):
    answer.append(dic[array[i]])

print(*answer)

