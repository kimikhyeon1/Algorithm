def solution(s):
    s_length = len(s)
    if s_length % 2 == 0:
        return s[s_length // 2 - 1 : s_length // 2 + 1]
    else:
        return s[s_length//2]