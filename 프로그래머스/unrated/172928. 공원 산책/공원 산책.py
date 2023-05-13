def solution(park, routes):
    graph = [[0]*len(park[0]) for _ in range(len(park))]
    start = []
    
    E = [0,1]
    S = [1,0]
    W = [0,-1]
    N = [-1,0]
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                graph[i][j] = 1
                start= [i,j]
            elif park[i][j] == "X":
                graph[i][j] = -1
    
    for i in routes:
        move = 0
        count = int(i.split()[-1])
        copy_start = start[:]

        if i[0] == "E":
            for i in range(count):
                if start[-1]+1 >= len(park[0]) or graph[start[0]][start[-1]+1] == -1:
                        start =copy_start[:]
                        break
                if start[-1]+1 < len(park[0]) and graph[start[0]][start[-1]+1] != -1:
                        start[-1]+=1
        elif i[0] == "S":
            for i in range(count):
                if start[0]+1 >= len(park) or graph[start[0]+1][start[-1]] == -1:
                        start = copy_start
                        break
                if start[0]+1 < len(park) and graph[start[0]+1][start[-1]] != -1:
                        start[0]+=1
        elif i[0] == "W":
            for i in range(count):
                if start[-1]-1 < 0 or graph[start[0]][start[-1]-1] == -1:
                    start = copy_start
                    break
                if start[-1]-1 >= 0 and graph[start[0]][start[-1]-1] != -1:
                    start[-1]-=1
        elif i[0] == "N":
            for i in range(count):
                if start[0]-1 < 0 or graph[start[0]-1][start[-1]] == -1:
                    start = copy_start
                    break
                if start[0]-1 >= 0  and graph[start[0]-1][start[-1]] != -1:
                    start[0]-=1
            
    return start