class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def DFS(i : int, j : int, visit : List[List[bool]], graph : List[List[str]]):     
            stack = [[i,j]]

            dx = [1,0,-1,0]
            dy = [0,1,0,-1]

            while stack:
                x, y = stack.pop()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                        if visit[nx][ny] == False and graph[nx][ny] == "1":
                            visit[nx][ny] = True
                            stack.append([nx,ny])  

            return

        answer = 0
        visit = [[False] * len(grid[0]) for _ in range(len(grid))] 


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visit[i][j] == False:
                    answer += 1
                    DFS(i,j,visit,grid)

        return answer

