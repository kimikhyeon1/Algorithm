def solution(n, slicer, num_list):
    start = slicer[0]
    end = slicer[1]
    index = slicer[2]

    if n == 1:
        return num_list[:end + 1]
    elif n == 2:
        return num_list[start:]
    elif n == 3:
        return num_list[start:end + 1]
    else:
        return num_list[start:end + 1:2]