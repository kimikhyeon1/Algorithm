import sys

input = sys.stdin.readline
n = int(input())
array = [list(map(int, input().strip())) for _ in range(n)]
visit = [[False]*n for _ in range(n)]

number = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def DFS(i,j):
    global number
    number+=1
    for k in range(4):
        nx = j + dx[k]
        ny = i + dy[k]
        if 0<=nx<n and 0<=ny<n:
            if array[ny][nx]==1 and visit[ny][nx]==False:
                visit[ny][nx]=True
                DFS(ny,nx)

answer_array = []

for i in range(n):
    for j in range(n):
        if array[i][j]==1 and visit[i][j]==False:
            visit[i][j] =True
            DFS(i,j)
            answer_array.append(number)
            number = 0


answer_array.sort()
print(len(answer_array))
for i in range(len(answer_array)):
    print(answer_array[i])