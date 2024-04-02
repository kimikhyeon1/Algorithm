def solution(s):
    array_s = s.split(" ")
    array = []
    
    for i in array_s:
        if i == "Z":
            array.pop()
            continue
        array.append(int(i))

    return sum(array)