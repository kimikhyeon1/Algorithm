def solution(array):
    answer = []
    max_num = 0
    for i in range(len(array)):
        if array[i] > max_num:
            max_num = array[i]
    answer.append(max_num)
    answer.append(array.index(max_num))
    return answer

