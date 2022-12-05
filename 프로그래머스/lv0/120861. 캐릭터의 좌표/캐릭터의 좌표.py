def solution(keyinput, board):
    answer = [0,0]

    for i in keyinput:
       
        if i =="up":
            if answer[1] == board[1]//2:
                continue
            else: answer[1] +=1
        elif i == "down":
            if answer[1] == -(board[1] // 2):
                continue
            else: answer[1] -=1
        elif i == "left":
            if answer[0] == -(board[0] // 2):
                continue
            else: answer[0] -=1
        elif i == "right":
            if answer[0] == (board[0] // 2):
                continue
            else: answer[0] +=1

        if board[0] == 1:
            answer[0]= 0

        if board[1] == 1:
            answer[1] = 0

    return answer
