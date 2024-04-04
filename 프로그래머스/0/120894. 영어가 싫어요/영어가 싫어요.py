def solution(numbers):
    answer = ""
    dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4",
           "five":"5", "six":"6", "seven":"7", "eight":"8", "nine": "9"}
    temp = ""
    for i in numbers:
        if temp in dic:
            answer += dic[temp]
            temp = ""
        temp += i
    
    answer += dic[temp]
        
    return int(answer)