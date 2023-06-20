# 간선의 개수를 구하면 된다.
import sys
import heapq
input = sys.stdin.readline
n = int(input())

for i in range(n):
    N, M = map(int,input().split())

    graph =  [[] for _ in range(N+1)]
    visit = [False] * (N+1)
    answer = 0
    for j in range(M):
        a,b = map(int,input().split())

        graph[a].append(b)
        graph[b].append(a)

    answer = N - 1
    print(answer)




