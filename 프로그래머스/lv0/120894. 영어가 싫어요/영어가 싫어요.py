def solution(numbers):
    answer = ""
    alp_space= ""
    for i in range(len(numbers)):
        alp_space += numbers[i]

        if alp_space =="one":
            alp_space = ""
            answer+="1"

        elif alp_space =="two":
            alp_space = ""
            answer+="2"

        elif alp_space =="three":
            alp_space = ""
            answer+="3"

        elif alp_space =="four":
            alp_space =""
            answer += "4"

        elif alp_space =="five":
            alp_space =""
            answer += "5"
        elif alp_space =="six":
            alp_space = ""
            answer += "6"

        elif alp_space =="seven":
            alp_space = ""
            answer += "7"

        elif alp_space =="eight":
            alp_space = ""
            answer += "8"

        elif alp_space == "nine":
            alp_space =""
            answer += "9"

        elif alp_space == "zero":
            alp_space = ""
            answer+="0"

    return int(answer)