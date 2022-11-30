from collections import deque
import sys
N= int(input())
array= deque([])
for i in range(N):
    x = sys.stdin.readline().rstrip()
    if x[0] =="e": #empty
        if len(array)==0: print(1)
        else: print(0)

    elif x[0] == "s":  # size
        print(len(array))

    elif x[0] == "f":  # front
        if len(array) == 0:
            print(-1)
        else:
            print(array[0])

    elif x[0] == "b":  # back
        if len(array) == 0:
            print(-1)
        else:
            print(array[-1])

    elif x[4]=="f": #pop_front
        if len(array) == 0: print(-1)
        else: print(array.popleft())

    elif x[4] =="b": #pop_back
        if len(array) == 0: print(-1)
        else: print(array.pop())

    elif x[5]=="b": #push_back
        array.append(int(x[10:]))

    elif x[5]=="f": #push_front
        array.appendleft(int(x[10:]))
