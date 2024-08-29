def solution(order):
    answer = 0
    for menu in order:
        if "ame" in menu:
            answer += 4500
            continue
        
        if "latte" in menu:
            answer += 5000
            continue
        
        answer += 4500
    return answer