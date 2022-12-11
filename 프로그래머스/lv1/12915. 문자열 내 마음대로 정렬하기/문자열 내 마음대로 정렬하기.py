def solution(strings, n):
    answer = strings
    
    for i in range(len(strings)):
        x=""
        
        for j in range(i+1,len(strings)):
            if ord(answer[i][n]) > ord(answer[j][n]):
                x=answer[i]
                answer[i] = answer[j]
                answer[j] = x
            elif ord(answer[i][n]) == ord(answer[j][n]):
                for k in range(len(answer[i])):
                    if ord(answer[i][k]) < ord(answer[j][k]):
                        break
                    elif ord(answer[i][k]) > ord(answer[j][k]):
                        x=answer[i]
                        answer[i] = answer[j]
                        answer[j] = x
                        break
                
    print(answer)
             
    return answer