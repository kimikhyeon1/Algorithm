def solution(lines):
    total_space = [0] * 202

    for i in range(lines[0][0]+1, lines[0][1] + 1):
        total_space[i + 100] += 1

    for i in range(lines[1][0]+1, lines[1][1] + 1):
        total_space[i + 100] += 1

    for i in range(lines[2][0]+1, lines[2][1] + 1):
        total_space[i + 100] += 1

    answer =0

    for i in range(1,len(total_space)):
        if total_space[i] > 1 :
            answer +=1

    return answer


print(solution([[1, 3], [1, 6], [1, 10]]))