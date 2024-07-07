def solution(s):
    if not (len(s) == 4 or len(s) == 6):
        return False;
    
    for i in s:
        if 48 <= ord(i) <= 57:
            continue
        return False
    
    return True 