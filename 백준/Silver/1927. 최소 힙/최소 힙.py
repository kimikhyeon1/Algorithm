import heapq
import sys

array = []
n = int(input())

for i in range(n):
    num = int(sys.stdin.readline())
    
    if num == 0:
        if len(array) == 0:
            print(0)
        else:
            print(heapq.heappop(array))
            
    else:
        heapq.heappush(array,num)

