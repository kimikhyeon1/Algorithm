import sys
input = sys.stdin.readline

N = int(input())
egg =[]
answer = 0

for _ in range(N):
    egg.append(list(map(int,input().split())))

# 1. 맨 오른쪽 계란까지 순서가 왔으면 return 총 깨진 개수
# 2. 이미 다 깨진 경우의 수가 나왔으면 종료
# 3. 이미 깨진 계란순서라면 넘어가기
# 4. 계란 깨기
def broken(number):
    global answer
    # 첫번쨰
    if number == N:
        broken_eggs = 0
        for i in range(N):
            if egg[i][0] <=0:
                broken_eggs+=1
        answer = max(answer,broken_eggs)
        return

    # 두번째
    if egg[number][0] <=0:
        broken(number+1)
        return

    # 세번째
    All_eggs_broken = True
    for i in range(N):
        if number == i:
            continue
        if egg[i][0] >0:
            All_eggs_broken = False
            break
    if All_eggs_broken:
        answer = max(answer,N-1)
        return

    # 네번째

    for i in range(N):
        if number==i or egg[i][0]<=0 :
            continue

        egg[number][0] -= egg[i][1]
        egg[i][0] -= egg[number][1]
        broken(number+1)
        egg[number][0] += egg[i][1]
        egg[i][0] += egg[number][1]

broken(0)
print(answer)