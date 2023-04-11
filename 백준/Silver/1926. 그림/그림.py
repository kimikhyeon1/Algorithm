import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(m)]
visit = [[False]*n for _ in range(m) ]

max_num=0
count=0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    num = 1

    while queue:
        y,x = queue.popleft()

        for k in range(4):
            nx = x+ dx[k]
            ny = y+ dy[k]

            if  0<= nx < n and 0 <= ny < m:
                if visit[ny][nx]==False and graph[ny][nx]==1:
                    queue.append((ny,nx))
                    visit[ny][nx] = True
                    num+=1


    return num



for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and visit[i][j] == False:
            visit[i][j] = True
            count+=1
            max_num=max(max_num,BFS(i,j))

print(count)
print(max_num)



