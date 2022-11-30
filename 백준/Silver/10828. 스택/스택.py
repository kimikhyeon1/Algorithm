import re
import sys

Num = int(input())
array =[]
for i in range(Num):
    Call = sys.stdin.readline()

    if Call[1] == "u":
        x = re.sub(r'[^0-9]', '', Call)
        array.append(int(x))

    elif Call[0] =="t":
        if len(array)>0:
            print(array[-1])
        else:
            print(-1)

    elif Call[0] =="s":
        print(len(array))

    elif Call[0] == "e":
        if len(array)==0:
            print(1)
        else:
            print(0)

    else:
        if len(array)>0:
            print(array.pop())
        else:
            print(-1)
