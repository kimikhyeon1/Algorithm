def solution(keyinput, board):
    answer = []
    x_limit = board[0] // 2
    y_limit = board[1] // 2
    x, y = 0, 0
    
    for i in keyinput:
        if i == "left":
            if x > (x_limit * -1):
                x -= 1
        elif i == "right":
            if x < x_limit:
                x += 1
        elif i == "up":
            if y < y_limit:
                y += 1
        elif i == "down":
            if y > (y_limit * -1):
                y -= 1
    
    return [x,y]