# 1. skip을 아스키코드로 변환해서 배열에 저장한다.
# 2. for 루프를 통해 아스키코드로 변환하여 index만큼 값을 올리고 skip이 포함되어있으면 스킵한다.
# 3. 아스키코드 범위를 넘으면 -25를 해준다.
# ord('a') = 97, + 25 = z 
def solution(s, skip, index):
    answer = ''
    skip_array = []
    
    for i in skip:
        skip_array.append(ord(i))

    for i in s:
        count = 0
        num = ord(i)
        
        while count < index:  
            num +=1 
            
            if num in skip_array:
                continue
                
            if num > 122:
                num -= 26
                if num in skip_array:
                    continue
                count += 1
                continue
                
            count +=1
            
        answer += chr(num)

    return answer