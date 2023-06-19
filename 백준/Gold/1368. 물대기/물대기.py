# 1. 입력받은 값을 graph 배열에 넣고 추가로 n값을 1개의 노드로 추가한다.

import heapq
import sys
n = int(input())
input = sys.stdin.readline
visit = [False] * (n+2)

answer = 0
array = []

for i in range(n):
    array.append(int(input()))
array.append(0)

graph = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    graph[i].append(array[i])

heap = [[0,1]]
graph.append(array)

while heap:
    weight, node = heapq.heappop(heap)

    if not visit[node]:
        visit[node] = True
        answer += weight

        for i,k in enumerate(graph[node-1]):
            if not visit[i+1]:
                heapq.heappush(heap,[k,i+1])

print(answer)




