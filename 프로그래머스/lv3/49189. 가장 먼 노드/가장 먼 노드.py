from collections import deque
def solution(n, edge):
    answer = 0
    tree = [[] for _ in range(n+1)]
    visit = [0] * (n + 1)
    
    for k,v in edge:
        tree[k].append(v)
        tree[v].append(k)
    
    def bfs(node):
        queae = deque([node])
        visit[1] = 1
        while queae:
            num = queae.popleft()
            
            for i in tree[num]:
                if visit[i] == 0:
                    visit[i] = visit[num] + 1
                    queae.append(i)
    
    bfs(1)
    max_num = max(visit)
    
    for i in visit:
        if i == max_num:
            answer +=1
    
    return answer