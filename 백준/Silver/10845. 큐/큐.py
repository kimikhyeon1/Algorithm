
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue =deque()

for i in range(N):
    ch = input().strip()

    if ch[-1] == "p":
        if len(queue):
            print(queue.popleft())
        else: print(-1)

    elif ch[-1] == "e":
        print(len(queue))

    elif ch[-1] == "y":
        if len(queue):
            print(0)
        else: print(1)

    elif ch[-1] == "t":
        if len(queue):
            print(queue[0])
        else: print(-1)

    elif ch[-1] == "k":
        if len(queue):
            print(queue[-1])
        else: print(-1)

    else:
        c, num = ch.split()
        queue.append(int(num))







