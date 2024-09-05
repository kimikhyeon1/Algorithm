def solution(n_str):
    answer = ''
    check_zero = False
    for number in n_str:
        if number == "0" and check_zero is False:
            continue
        else:
            check_zero = True
        answer += number
    return answer