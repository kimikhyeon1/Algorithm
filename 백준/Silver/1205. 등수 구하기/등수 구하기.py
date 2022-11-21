import sys

read = lambda : sys.stdin.readline().rstrip()

a,b,c =map(int,read().split())
score = []
if a:
    score = list(map(int,read().split()))

score.append(b)
score.sort(reverse=True)
place = 0
count = 0

for i in range(len(score)):
    if b == score[i]:
       count += 1

for i in range(len(score)):
    if score[i] == b:
        place = i + 1

if place > c:
    print(-1)
    exit()

print(place - (count - 1))