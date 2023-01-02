
from collections import deque



def bfs(x,y):
    each = 1
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]

            if 0<=nx<n and 0<=ny<m:
                if array[nx][ny] ==1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    each +=1
                    queue.append((nx,ny))

    return each


n,m = map(int,input().split())
visited = [[False] * m for _ in range(n)]
array = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt , maxcnt =0,0
for i in range(n):
    for j in range(m):
        if array[i][j]==1 and not visited[i][j]:
            cnt+=1
            maxcnt = max(maxcnt , bfs(i,j))




print(cnt)
print(maxcnt)