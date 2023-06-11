import sys
input = sys.stdin.readline

N, M = map(int,input().split())
array = list(map(int,input().split()))

start = 0
end = 0

answer = sys.maxsize
num = 0

while True:
    if num >= M:
        answer = min(end-start, answer)
        num -= array[start]
        start += 1

    elif end == len(array):
        break

    else:
        num += array[end]
        end += 1

if answer != sys.maxsize:
    print(answer)
else:
    print(0)