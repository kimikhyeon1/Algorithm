import sys
input = sys.stdin.readline

N,M = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
answer = []
visit = [False] * N
x = 0
def dfs(number):
    global answer
    global x

    if len(answer)==M :
        print(*answer)
        return

    for i in range(number,N):
        if visit[i] == True:
            continue
        if x == array[i]:
            continue

        answer.append(array[i])
        visit[i] = True
        dfs(i+1)
        x = answer.pop()
        visit[i] = False

dfs(0)