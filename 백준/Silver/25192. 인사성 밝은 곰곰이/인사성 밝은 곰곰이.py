import sys
input = sys.stdin.readline

N = int(input())

count = 0
check_array = {}
for i in range(N):
    comment = input().strip()

    if comment == "ENTER":
        count += len(check_array)

        check_array = {}
        continue

    if comment in check_array:
        check_array[comment] +=1
    else:
        check_array[comment] = 1
        
count += len(check_array)

print(count)

