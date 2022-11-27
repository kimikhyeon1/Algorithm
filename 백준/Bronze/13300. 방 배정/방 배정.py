# 수학여행 학생 수 n과  한방 최대인원 K 가 주어진다
# 각 줄에는 성별 S와 학년 Y가 주어진다 0은 여자 1은 남자
# 학년별로 남 여 를 구분한 후 K에 맞게 count를 추가한다.


N, K = map(int,input().split())

men = [0]*6
women = [0]*6
for i in range(N):
    x,y = map(int,input().split())
    if x ==0:
        women[y-1] +=1
    else:
        men[y-1] +=1

room_count = 0

for i in men:
    while i >0:
        i -= K
        room_count+=1

for i in women:
    while i >0:
        i -= K
        room_count+=1

print(room_count)