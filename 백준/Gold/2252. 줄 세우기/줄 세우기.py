from collections import deque

v, e = map(int,input().split())

indegree = [0]* (v+1)
graph = [[] for _ in range(v+1)]
for i in range(e):
    x, y = map(int,input().split())
    graph[x].append(y)
    indegree[y] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        num = q.popleft()
        result.append(num)

        for i in graph[num]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i,end=" ")

topology_sort()