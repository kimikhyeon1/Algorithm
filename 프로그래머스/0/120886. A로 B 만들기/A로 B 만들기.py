def solution(before, after):
    a = []
    b = []
    for i in range(len(before)):
        a.append(before[i])
        b.append(after[i])
    a.sort()
    b.sort()
    print(a,b)
    if a == b:
        return 1
    else:
        return 0