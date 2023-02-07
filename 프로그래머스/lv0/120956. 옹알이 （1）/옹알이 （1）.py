from collections import deque


def solution(babbling):
    babbling_list = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in range(len(babbling)):
        if babbling[i] in babbling_list:
            answer+=1
            continue
        queue = deque(babbling[i])
        length = len(queue)
        print(queue)
        start=0
        three_end=3
        two_end =2
        for j in range(len(babbling[i])):
            if len(queue)>2 and babbling[i][start:three_end] in babbling_list:
                queue.popleft()
                queue.popleft()
                queue.popleft()
                length -=3
                start+=3
                three_end+=3
                two_end+=3

            elif len(queue)>1 and babbling[i][start:two_end] in babbling_list:
                queue.popleft()
                queue.popleft()
                length-=2
                start += 2
                three_end +=2
                two_end += 2

            if length ==0:
                answer +=1
                break

    return answer