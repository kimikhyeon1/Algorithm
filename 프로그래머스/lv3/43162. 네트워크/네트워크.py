from collections import deque

def bfs(node):
    global answer, tree, visit
    queae = deque()
    queae.append(node)
    answer += 1 
    
    while queae:
        num = queae.popleft()
        for i in tree[num]:
            if not visit[i]:
                visit[i] = True
                queae.append(i)


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
                bfs(i)
                
    return  answer