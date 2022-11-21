a = int(input())
sum = 1
answer=0
count =0
while True:
    answer +=sum
    sum+=1
    count +=1
    if answer >a:
        print(count-1)
        break