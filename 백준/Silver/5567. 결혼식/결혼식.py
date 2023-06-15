import sys
input = sys.stdin.readline

N= int(input())
M = int(input())

tree = [[] for _ in range(N+1)]

for i in range(M):
    V, E = map(int,input().split())
    tree[V].append(E)
    tree[E].append(V)

first = tree[1]

array = []
for i in first:
    array += tree[i]
answer = set(array+first)

if 1 in answer:
    print(len(answer)-1)
else:
    print(len(answer))