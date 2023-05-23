import heapq
from collections import deque

N, K = map(int,input().split())

array = [i for i in range(1,N+1)]

queue = deque(array)
answer = []
while queue:
    for _ in range(K-1):
        array.append(queue.append(queue.popleft()))
    answer.append(queue.popleft())

print("<",end="")
for i in answer:
    if i ==answer[-1]:
        print(i,end="")
        break
    print(i,end=", ")
print(">")