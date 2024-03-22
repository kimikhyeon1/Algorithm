def solution(num, k):
    array = []
    for i in str(num):
        array.append(i)
    for i in range(len(array)):
        if array[i] == str(k):
            return i + 1
        
    return -1