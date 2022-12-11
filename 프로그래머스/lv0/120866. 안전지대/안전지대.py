from collections import deque
def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    visited = [[False] * m for _ in range(n)]
    dx = [1, 0, -1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, 1, -1, - 1, 1]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < m:
                            visited[nx][ny] = True

    for i in range(n):
        for j in range(m):
            if visited[i][j] == False:
                answer += 1
    return answer