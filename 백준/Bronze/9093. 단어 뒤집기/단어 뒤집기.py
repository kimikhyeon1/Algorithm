import sys

input = sys.stdin.readline

N = int(input())
for i in range(N):
    str = list(input().split())
    for j in str:
        print(j[::-1],end=" ")