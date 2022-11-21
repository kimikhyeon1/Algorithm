import re

while True:
    str = input().rstrip()

    if str == ".":
        break

    q_array = re.findall('\[|\]|\(|\)', str)

    if len(q_array) ==0:
        print("yes")
        continue

    array_total = []


    for i in range(len(q_array)):
        if q_array[i] == "(":
            array_total.append(q_array[i])

        elif q_array[i] == ")":
            if len(array_total) ==0:
                print("no")
                break
            elif array_total[-1] !="(":
                print("no")
                break
            else:
                array_total.pop()

        elif q_array[i] == "[":
            array_total.append(q_array[i])

        elif q_array[i] == "]":
            if len(array_total) == 0:
                print("no")
                break

            elif array_total[-1] != "[":
                print("no")
                break
            else:
                array_total.pop()

        if len(q_array)-1 == i:
            if len(array_total) ==0 :
                    print("yes")
            else: print("no")