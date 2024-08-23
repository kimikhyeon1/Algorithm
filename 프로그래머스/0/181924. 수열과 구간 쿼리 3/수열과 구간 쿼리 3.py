def solution(arr, queries):
    for index in queries:
        temp = arr[index[0]]
        arr[index[0]] = arr[index[1]]
        arr[index[1]] = temp
    return arr