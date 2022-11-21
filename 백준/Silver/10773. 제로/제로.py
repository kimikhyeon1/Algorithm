

K = int(input())

array = []
for i in range(K):
    num = int(input())
    if num >0:
        array.append(num)
    else:
        array.pop()
sum = 0
for i in range(len(array)):
    sum +=array[i]

print(sum)