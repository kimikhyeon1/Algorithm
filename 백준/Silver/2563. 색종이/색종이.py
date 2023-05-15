N = int(input())
graph = [[0]*100 for _ in range(100)]

def paper(x,y):
    for i in range(x,x+10):
        for j in range(y,y+10):
            graph[i][j]+=1

for i in range(N):
    x,y = map(int,input().split())
    paper(x,y)

answer =0
for i in range(100):
    for j in range(100):
        if graph[i][j] > 0:
            answer +=1

print(answer)