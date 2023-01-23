from collections import deque

N,M = map(int,input().split())

array = []

for i in range(N):
    array.append(list(map(int,input())))


def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if array[nx][ny] == 0:
                continue

            if array[nx][ny]==1:
                array[nx][ny]= array[x][y]+1
                queue.append((nx,ny))

    return array[N-1][M-1]

print(bfs(0,0))