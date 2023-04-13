import sys
input = sys.stdin.readline

N,M = map(int,input().split())
X = list(map(int,input().split()))
X.sort()
answer=[]

def dfs():
    if len(answer) == M:
        print(' '.join(map(str,answer)))
        return

    for i in X:
        if i not in answer:
            answer.append(i)
            dfs()
            answer.pop()

dfs()