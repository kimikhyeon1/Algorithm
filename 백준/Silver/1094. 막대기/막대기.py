N = int(input())
count = 0
stick = [64,32,16,8,4,2,1]
for i in range(7):
    if N >= stick[i]:
        N -= int(stick[i])
        count +=1

print(count)