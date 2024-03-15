def solution(cipher, code):
    answer = ''
    array = [0]
    for i in cipher:
        array.append(i)
    for i in range(1,len(array)):
        if i % code == 0:
            answer += array[i]
    return answer