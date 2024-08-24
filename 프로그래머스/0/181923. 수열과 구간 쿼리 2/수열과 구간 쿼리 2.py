def solution(arr, queries):
    answer = []
    for array in queries:
        start = array[0]
        end = array[1]
        target = array[2]
        
        find = False
        for num in sorted(arr[start:end+1]):
            if num > target:
                answer.append(num)
                find = True
                break
        
        if not find:
            answer.append(-1)
    return answer