import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N= int(input())
visit = [False] * (N+1)
graph = [[] for _ in range(N+1)]
answer = [[] for _ in range(N+1)]

for i in range(N-1):
    v, e = map(int,input().split())
    graph[v].append(e)
    graph[e].append(v)

def dfs(node):
    for i in graph[node]:
        if not visit[i]:
            visit[i] = True
            dfs(i)
            answer[i] = node

dfs(1)

for i in range(2,N+1):
    print(answer[i])

