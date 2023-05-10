import sys

input = sys.stdin.readline
N,M = map(int,input().split())

array = {}
reverse_array = {}
for i in range(N):
    solve = input().strip()
    array[solve] = i+1
    reverse_array[i+1]=solve

for i in range(M):
    answer = input().strip()
    if 47<ord(answer[0])<58:
        print(reverse_array[int(answer)])
    else:
        print(array[answer])


