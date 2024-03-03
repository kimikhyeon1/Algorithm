def solution(numbers):
    sorted_array = sorted(numbers, reverse = True)
    return sorted_array[0] * sorted_array[1]