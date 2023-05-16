"""
 1. 입력받은 N의 정수만큼 for문 실행
 2. 조건문을 통해 입력받은 문자를 해석
    2-1 L이면 포인터를 왼쪽으로 이동 (point -=1)
    2-2 D이면 포인터를 오른쪽으로 이동 (point +=1)
    2-3 B이면 포인터 왼쪽 문자 삭제 (만약, 포인터가 0이면 삭제하지 않는다)
    2-4 P $이면 포인터 왼쪽에 문자 추가
"""

import sys

input = sys.stdin.readline

stack1= list(input().strip())
stack2 = []
N = int(input())

for i in range(N):
    ch = list(input().strip())
    if len(ch)>1:
        stack1.append(ch[-1])
    elif "L" in ch:
        if stack1:
            stack2.append(stack1.pop())
    elif "D" in ch:
        if stack2:
            stack1.append(stack2.pop())
    elif "B" in ch:
        if stack1:
            stack1.pop()

stack1.extend(reversed(stack2))
print("".join(stack1))



