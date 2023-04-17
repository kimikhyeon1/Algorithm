import sys
input = sys.stdin.readline

N,M = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
answer = []
x=0
def dfs(number):
    global x
    if len(answer)==M:
        print(*answer)
        return

    for i in range(number,N):
        if x ==array[i]:
            continue
        answer.append(array[i])
        dfs(i)
        x = answer.pop()
dfs(0)
