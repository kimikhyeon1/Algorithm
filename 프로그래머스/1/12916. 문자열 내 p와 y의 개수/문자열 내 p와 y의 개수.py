def solution(s):
    countP = 0
    countY = 0
    
    for i in s:
        if i == 'p' or i == 'P':
            countP += 1
            continue
        if i == 'y' or i == 'Y':
            countY += 1

    return countP == countY