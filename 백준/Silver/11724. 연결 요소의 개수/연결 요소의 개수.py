from collections import deque
import sys
input = sys.stdin.readline

v,e = map(int,input().split())

graph = [[] for _ in range(v+1)]
visit = [False] * (v+1)

for _ in range(e):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def bfs(i):
    queue = deque([i])

    while queue:
        x = queue.popleft()
        for j in graph[x]:
            if visit[j] == False:
                visit[j] = True
                queue.append(j)

count = 0

for i in range(1,v+1):
    if visit[i] == False:
        count += 1
        visit[i] = True
        bfs(i)

print(count)