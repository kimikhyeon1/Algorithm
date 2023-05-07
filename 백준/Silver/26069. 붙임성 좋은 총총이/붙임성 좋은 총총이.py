import sys
input = sys.stdin.readline

N = int(input())

count = 0
check_array = set()
meet_chongchong = False

for i in range(N):
    a, b = input().split()

    if a== "ChongChong" or b == "ChongChong":
        check_array.add(a)
        check_array.add(b)
        meet_chongchong = True

    if not meet_chongchong:
        continue

    if a in check_array or b in check_array:
        check_array.add(a)
        check_array.add(b)



print(len(check_array))