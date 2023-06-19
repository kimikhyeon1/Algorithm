import heapq
import sys
v, e = map(int,input().split())
input = sys.stdin.readline
graph = [[] for _ in range(v+1)]
visit = [False] * (v+1)

for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

heap = [[0,1]]
answer = 0

while heap:
    weight, node = heapq.heappop(heap)

    if not visit[node]:
        answer += weight
        visit[node] = True

        for i in graph[node]:
            if not visit[i[1]]:
                heapq.heappush(heap,i)

print(answer)

