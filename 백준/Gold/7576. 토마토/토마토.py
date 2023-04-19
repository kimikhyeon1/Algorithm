import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(M)]
queue = deque([])
dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = 0
for i in range(M):
    for j in range(N):
        if array[i][j]==1:
            queue.append([i,j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<M and 0<=ny<N and array[nx][ny] ==0 :
                array[nx][ny]= array[x][y]+1
                queue.append([nx,ny])

bfs()

for i in array:
    for j in i:
        if j == 0:
            print(-1)
            quit()
        answer = max(j,answer)

print(answer-1)
