def solution(numbers, k):
    count = 0
    for i in range(k-1):
        count += 2
        if count >= len(numbers):
            count -= len(numbers)
        
    return numbers[count]