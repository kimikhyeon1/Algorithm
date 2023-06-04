# 머지소트를 구현해 보곘습니다..
import sys
input = sys.stdin.readline
N = int(input())
array=[]
for i in range(N):
    array.append(int(input()))
def merge_sort(array):
    if len(array) == 1:
        return array

    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]

    left_array = merge_sort(left)
    right_array = merge_sort(right)

    result_array = []
    left_point = 0
    right_point = 0

    while len(left_array) > left_point or len(right_array) > right_point:
        if len(left_array) == left_point:
            result_array.append(right_array[right_point])
            right_point+=1
            continue
        elif len(right_array) == right_point:
            result_array.append(left_array[left_point])
            left_point+=1
            continue

        if left_array[left_point] <= right_array[right_point]:
            result_array.append(right_array[right_point])
            right_point+=1
        else:
            result_array.append(left_array[left_point])
            left_point+=1

    return result_array

answer_array = merge_sort(array)

for i in answer_array:
    print(i)
