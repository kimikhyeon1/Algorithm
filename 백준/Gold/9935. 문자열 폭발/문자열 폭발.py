import sys
first_str = sys.stdin.readline().strip()
second_str = sys.stdin.readline().strip()

length = len(second_str)
answer = []
while True:
    for i in first_str:
        answer.append(i)
        if i==second_str[-1]  and "".join(answer[-length:]) == second_str:
            del answer[-length:]
            continue
    break


if len(answer) ==0:
    print("FRULA")
else:
    print("".join(answer))