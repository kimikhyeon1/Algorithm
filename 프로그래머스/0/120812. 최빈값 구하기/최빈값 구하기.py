def is_double(dic, max_num, max_value):
    double_check = 0
    for k, v in dic.items():
        if v == max_value:
            double_check += 1
    
    if double_check > 1:
        return False
    
    return True

def solution(array):
    dic = {}
    for i in array:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    max_value = 0
    max_num = 0
    for k, v in dic.items():
        if max_value < v:
            max_value = v 
            max_num = k
                        
    if is_double(dic,max_num, max_value):
        return max_num
    
    return -1