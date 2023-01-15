def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12

    for i in numbers:
        if i in [1,4,7]:
            answer+="L"
            left = i
        elif i in [3,6,9]:
            answer+="R"
            right = i
        else:
            if i==0: i=11
            left_p = (abs(i-left)//3)+(abs(i-left)%3)
            right_p = (abs(i-right)//3)+(abs(i-right)%3)

            if left_p == right_p:
                if hand =="right":
                    answer+="R"
                    right = i
                else:
                   answer+="L"
                   left = i

            elif left_p < right_p:
                answer += "L"
                left = i
            else:
                answer += "R"
                right = i

    return answer