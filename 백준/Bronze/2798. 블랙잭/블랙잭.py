N, target = map(int,input().split())
array = list(map(int,input().split()))

count = 0
answer = 0
def bfs(index,csum):
    global count
    global answer
    if csum > target:
        return
    if count ==3:
        answer = max(answer,csum)
        return

    for i in range(index,N):
        count+=1
        bfs(i+1,csum+array[i])
        count-=1

bfs(0,0)

print(answer)