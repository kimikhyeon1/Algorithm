from collections import deque

def dfs(node):
    global answer, tree, visit
    
    for i in tree[node]:
        if not visit[i]:
            visit[i] = True
            dfs(i)
        


def solution(n, computers):
    global answer, tree, visit
    answer = 0
    tree = [[]  for _ in range(n+1)]
    visit = [False] * (n+1)
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                tree[i+1].append(j+1)
    
    for i in range(1,n+1):
        for j in tree[i]:
            if visit[j] == False:
                answer += 1
                dfs(i)
                
    return  answer