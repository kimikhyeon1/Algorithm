from collections import deque

num = int(input())
array = deque([])
for i in range(num):
    array.append(i+1)

if len(array)==1:
    print(array[0])
    exit()
while True:
    array.popleft()
    if len(array)==1:
        print(array[0])
        exit()
    x =array.popleft()
    array.append(x)
    if len(array)==1:
        print(array[0])
        exit()