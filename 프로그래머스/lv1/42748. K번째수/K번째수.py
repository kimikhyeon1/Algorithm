def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        array1 = commands[i]
        if array1[0]==array1[1]:
            answer.append(array[array1[0]-1])
            continue
        space = array[array1[0]-1:array1[1]]
        space.sort()
        answer.append(space[array1[2]-1])

    return answer