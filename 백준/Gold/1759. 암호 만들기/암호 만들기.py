import sys
input = sys.stdin.readline

N,M = map(int,input().split())
array = list(input().split())
array.sort()
answer = []
def dfs(number):
    if len(answer) == N and ("a" in answer or "e" in answer or "i" in answer or "o" in answer or "u" in answer):
        count = 0
        for char in answer:
            if char not in 'aeiou':
                count+=1
        if count > 1:
            print("".join(answer))
        return

    for i in range(number,M):
        answer.append(array[i])
        dfs(i+1)
        answer.pop()
dfs(0)
