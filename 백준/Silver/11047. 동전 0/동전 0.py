import sys

input = sys.stdin.readline

N, money = map(int,input().split())

array = []
for i in range(N):
    array.append(int(input()))

count = 0

while money:
    x = 0
    for i in range(len(array)):
        if array[i] <= money:
            x+=1

    y = money // array[x-1]
    count += money//array[x-1]
    money = money - (y*array[x-1])

print(count)


