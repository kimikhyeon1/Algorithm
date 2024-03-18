def solution(nums):
    answer = 0
    dic = {}
    for i in nums:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    count = len(nums) // 2
    
    if len(dic) > count:
        answer = count
    else:
        answer = len(dic)
    return answer