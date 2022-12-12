def solution(n, arr1, arr2):
    array1 = []
    array2 = []
    change_int_array = []

    for i in range(n):
        change_int1 = format(arr1[i], "b")
        change_int2 = format(arr2[i], "b")
        if len(change_int1) ==n-1:
            array1.append("0" + change_int1)
            array2.append("0" + change_int2)
        else:
            array1.append(change_int1)
            array2.append(change_int2)

    for i in range(n):
        change_int_array.append(str(int(array1[i])+int(array2[i])))
        if len(change_int_array[i]) != n:
            count = n-len(change_int_array[i])
            change_int_array[i]="0"*count +change_int_array[i]

    str_space = ""

    for i in range(len(change_int_array)):
        for j in range(n):
            if int(change_int_array[i][j]) >=1:
                str_space+= "#"
            else:
                str_space+= " "
    count = 0
    text = ""
    answer = []
    while count < len(str_space):
        if count%n == 0 and count:
            answer.append(text)
            text=""

        text += str_space[count]
        count+=1

        if count== len(str_space):
            answer.append(text)

    return answer