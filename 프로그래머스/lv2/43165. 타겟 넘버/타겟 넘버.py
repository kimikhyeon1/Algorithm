def solution(numbers, target):
    global answer
    answer = 0
    def dfs(idx, number):
        global answer
        if idx == len(numbers) and target == number:
            answer += 1
            return
        elif idx == len(numbers):
            return
        
        dfs(idx+1,number+numbers[idx])   
        dfs(idx+1,number-numbers[idx])
    
    dfs(0,0)
            
    return answer