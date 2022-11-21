n = int(input())
array = list(map(int,input().split()))
array.sort()
sum = int(input())
count = 0
start ,end = 0,n-1
while start<end:
    if sum == array[start]+array[end]:
        count+=1

    if sum > array[start]+array[end]:
        start+=1
        continue
    end -=1
print(count)