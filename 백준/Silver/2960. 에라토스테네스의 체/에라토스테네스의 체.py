A,B = map(int,input().split())

nums = [True]*1005
count =0

for i in range(2,len(nums)+1):
    for j in range(i,A+1,i):
        if nums[j] == True:
            nums[j] = False
            count += 1

        if count ==B:
            print(j)
            exit()