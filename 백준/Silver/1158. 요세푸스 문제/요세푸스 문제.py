
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int,input().split())

queue = deque(i for i in range(1,N+1))
answer_array = []
count=1
while queue:
    if count == K or len(queue) == 1:
        count = 1
        answer_array.append(queue.popleft())
        continue

    first = queue.popleft()
    queue.append(first)
    count+=1

print("<",end="")
for i in answer_array:
    if i == answer_array[-1]:
        print(i,end="")
        break
    print(i,end=", ")


print(">")
