N= int(input())
flo = map(int,input().split())
answer=0
for i in flo:
    error = 0
    if i>1:
        for k in range(2,i):
            if i%k==0:
                error +=1
        if error ==0:
            answer+=1

print(answer)
