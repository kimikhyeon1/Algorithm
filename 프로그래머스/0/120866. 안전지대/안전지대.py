def solution(board):
    answer = 0
    
    nx = [0,1,-1,0,1,1,-1,-1]
    ny = [1,0,0,-1,1,-1,1,-1]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                for k in range(8):
                    x = nx[k] + j
                    y = ny[k] + i
                    
                    if x >= 0 and y >= 0 and x < len(board[0]) and y < len(board):
                        if board[y][x] == 0:
                            board[y][x] = 2
                            
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                answer += 1

    return answer