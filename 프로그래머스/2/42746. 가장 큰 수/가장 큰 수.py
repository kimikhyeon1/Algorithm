def solution(numbers):
    answer = ''
    array = {}
    
    for index, i in enumerate(numbers):
        number = str(i)+str(i)+str(i)+str(i)
        array[index] = int(number[:4])
    
    array = sorted(array.items(), key = lambda x:x[1],reverse = True)
    
    for data in array:
        answer += str(numbers[data[0]])
    
    if int(answer) == 0:
        return "0"

    return answer