L, R = input().split()
count = 0
if len(L)<len(R):
    print(0)
    exit()
elif len(L)==len(R):
    for i in range(len(R)):
        if L[i]!=R[i] :
            break
        count +=1
answer =0
for i in range(count):
    if R[i]=="8":
        answer +=1
print(answer)
