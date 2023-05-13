def solution(n, m, section):
    answer = 0
    array = [False]*(n+1)
    for i in section:
        array[i] = True
    x = False
    count = 1
    for i in range(len(array)):
        
        if count ==m:
            count = 1
            x = False
            
        if x == True:
            array[i] = False
            count +=1
            continue
            
        if array[i]==True:
            x= True
            array[i]=False
            answer+=1
            
    return answer