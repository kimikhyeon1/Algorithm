import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
dx =[1,0,-1,0]
dy =[0,1,0,-1]

def BFS(x,y):
    visit[x][y] = True
    alp = rgb_graph[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx< N and 0 <= ny < N:
            # 현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs로 넣어준다.
            if visit[nx][ny] == False:
                if rgb_graph[nx][ny] == alp:
                    BFS(nx, ny)
    # queue = deque()
    # queue.append((x,y))
    # dx =[1,0,-1,0]
    # dy =[0,1,0,-1]
    #
    # alp = 0
    # while queue:
    #     a,b = queue.popleft()
    #     visit[a][b]=True
    #     alp = rgb_graph[a][b]
    #
    #     for i in range(4):
    #         nx = a + dx[i]
    #         ny = b + dy[i]
    #
    #         if 0<=nx< N and 0 <= ny < N:
    #             if rgb_graph[nx][ny] == alp and visit[nx][ny] != True:
    #                 queue.append((nx,ny))


N = int(input().rstrip())
rgb_graph = [list(input().rstrip()) for _ in range(N)]
visit = [[False]*N for _ in range(N)]
RGB = 0
RB = 0

for i in range(N):
    for j in range(N):
        if visit[i][j] != True:
            RGB +=1
            BFS(i,j)


for i in range(N):
    for j in range(N):
        if rgb_graph[i][j] == "G":
            rgb_graph[i][j] = "R"

visit = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visit[i][j] != True:
            RB +=1
            BFS(i,j)

print(RGB,RB)
