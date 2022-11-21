x = int(input())

hansu=0
for i in range(1,x+1):
    num1 = list(map(int, str(i)))
    if i < 100:
        hansu +=1
    elif (num1[0]-num1[1]) == (num1[1] -num1[2]):
        hansu +=1

print(hansu)