def solution(num_list, n):
    answer = []
    count =0
    range = len(num_list)//n
    fix_num = n
    change_num = n
    while count<range:
        if count==0:
            answer.append(num_list[:n])
            change_num+=n
            count+=1
        else:
            answer.append(num_list[n:change_num])
            count+=1
            n+= fix_num
            change_num+= fix_num
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8],2))

print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948],3))