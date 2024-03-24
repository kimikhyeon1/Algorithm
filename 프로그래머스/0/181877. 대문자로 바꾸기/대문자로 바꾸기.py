def solution(myString):
    answer = ''
    for i in range(97,100):
        print(chr(i))
    for i in myString:
        if ord(i) > 96:
            answer += chr(ord(i) - 32)
        else:
            answer += i
    return answer