def solution(board, h, w):
    answer = 0
    color = board[h][w]
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    for i in range(4):
        x = h + dx[i]
        y = w + dy[i]
        
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            continue
            
        if board[x][y] == color:
            answer += 1
            
    return answer