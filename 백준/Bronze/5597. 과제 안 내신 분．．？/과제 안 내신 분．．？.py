array = []

for i in range(30):
    array.append(i+1)

for i in range(28):
    array.remove(int(input()))

array.sort()
for i in array:
    print(i)