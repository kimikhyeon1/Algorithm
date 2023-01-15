def solution(food):
    answer = ''

    for i in range(len(food)):
        if i ==0:
            continue
        count = (food[i]//2)
        while(count):
            answer+=str(i)
            count-=1

    for i in range(len(answer),0,-1):
        if i ==len(answer):
            answer+="0"
        answer += str(answer[i-1])

    return answer