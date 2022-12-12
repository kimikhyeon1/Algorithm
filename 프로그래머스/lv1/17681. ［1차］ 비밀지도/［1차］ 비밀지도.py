def solution(n, arr1, arr2):
    array1 = []
    array2 = []
    change_int_array = []

    for i in range(n):
        change_int1 = format(arr1[i],"b")
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

    last_answer = ""

    for i in range(len(change_int_array)):
        for j in range(n):
            if int(change_int_array[i][j]) >=1:
                last_answer+= "#"
            else:
                last_answer+= " "
    count = 0
    text = ""
    ze = []
    while count < len(last_answer):
        if count%n == 0 and count:
            ze.append(text)
            text=""

        text += last_answer[count]
        count+=1

        if count== len(last_answer):
            ze.append(text)

    return ze