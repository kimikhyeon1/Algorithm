def solution(strings, n):
    answer = strings
    for i in range(len(strings)):
        x=""
        for j in range(i+1,len(strings)):
            if ord(answer[i][n]) > ord(answer[j][n]): 
                #i번쨰의 n번째 index와 j번째의n번쨰 인덱스를 비교한다.
                #만약 i번째가 더 큰 알파벳이면 j번쨰와 위치를 바꾼다. 
                x=answer[i]  
                answer[i] = answer[j]
                answer[j] = x
            elif ord(answer[i][n]) == ord(answer[j][n]):
                #만약 i번째 n번째 index와 j가 같다면
                #첫번쨰 인덱스부터 비교를 해야한다.
                for k in range(len(answer[i])):
                    if ord(answer[i][k]) < ord(answer[j][k]):
                        break
                    #i와 j의 첫번째 인덱스 부터 비교해서 만약 j의 알파벳 크기가 더 크면
                    #그대로 종료한다.
                    elif ord(answer[i][k]) > ord(answer[j][k]):
                    #i가 j보다 알파벳 크기가 더 크면 위치를 변경하고 종료한다.
                        x=answer[i]
                        answer[i] = answer[j]
                        answer[j] = x
                        break            
    print(answer)
             
    return answer