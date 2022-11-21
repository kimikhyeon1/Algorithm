count = 0
N= int(input())

while N>2:
    if N%5 ==0:
        count += N//5
        N=0
        break
    N -= 3
    count +=1

if N!=0: print(-1)

else: print(count)