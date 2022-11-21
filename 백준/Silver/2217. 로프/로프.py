N = int(input())
k = []
for i in range(N):
    k.append(int(input()))
k.sort()
res = 0
for i in range(N):
    if res<k[i]*(N-i):
        res = k[i]*(N-i)
print(res)