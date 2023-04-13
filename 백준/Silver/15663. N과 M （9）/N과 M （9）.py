import sys
input = sys.stdin.readline

N,M = map(int,input().split())
X = list(map(int,input().split()))
X.sort()
answer=[]
space=[]
visit = [False]*N

def dfs():
    # if list(answer) in space:
    #     return

    if len(answer) == M:
        # space.append(list(answer))
        print(' '.join(map(str,answer)))
        return
    a=0
    for i in range(N):
        if visit[i]==False and a!=X[i]:
            visit[i]=True
            answer.append(X[i])
            a=X[i]
            dfs()
            answer.pop()
            visit[i]=False

dfs()
