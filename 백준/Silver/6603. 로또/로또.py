import sys
input = sys.stdin.readline

def dfs(number):

    if len(array) == 6:
        print(*array)
        return

    for i in range(number,K):
        if visit[i] == True:
            continue

        visit[i] = True
        array.append(S[i])
        dfs(i)
        visit[i] = False
        array.pop()


while True:
    input_data = list(map(int,input().split()))

    if input_data[0] ==0:
        break

    K = input_data[0]
    S = input_data[1:]
    array = []
    visit = [False] * K
    dfs(0)
    print("")