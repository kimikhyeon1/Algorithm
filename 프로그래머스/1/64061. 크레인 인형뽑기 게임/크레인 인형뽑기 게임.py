def solution(board, moves):
    answer = 0
    stack = []
    change_board = []
    
    for i in range(len(board)):
        dolls = []
        
        for j in range(len(board[0]) - 1 , -1, -1):
            if board[j][i] != 0:
                dolls.append(board[j][i])
                
        change_board.append(dolls)
        
    for item in moves:
        if len(change_board[item - 1]) == 0:
            continue
        
        doll = change_board[item - 1].pop()
        
        if len(stack) == 0:
            stack.append(doll)
            continue
        
        if stack[-1] == doll:
            stack.pop()
            answer += 2
            
            while len(stack) > 1 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
        else:
            stack.append(doll)
            
    return answer


