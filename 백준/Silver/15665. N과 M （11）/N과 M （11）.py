import sys
input = sys.stdin.readline

N,M = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
answer = []
def dfs():
    global x
    x = 0
    if len(answer)==M:
        print(*answer)
        return

    for i in range(N):
        if x ==array[i]:
            continue
        answer.append(array[i])
        dfs()
        x = answer.pop()
dfs()
