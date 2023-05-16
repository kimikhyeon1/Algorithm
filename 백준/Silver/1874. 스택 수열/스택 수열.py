import sys

input = sys.stdin.readline

N = int(input())
def stack():
    stack = []
    array = [1]
    answer = ["+"]
    count=2
    for i in range(N):
        num = int(input())
        stack.append(num)

        while count <= num:
            array.append(count)
            count+=1
            answer.append("+")

        if array[-1] == stack[-1]:
            stack.pop()
            array.pop()
            answer.append("-")

    if stack:
        return ["NO"]
    else:
        return answer

l = stack()

for i in l:
    print(i)