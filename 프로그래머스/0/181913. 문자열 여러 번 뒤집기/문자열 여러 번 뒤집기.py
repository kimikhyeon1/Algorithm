def solution(my_string, queries):
    for array in queries:
        start = array[0]
        end = array[1] + 1
        reverse_string = ''.join(reversed(my_string[start:end]))
        my_string = my_string[:start] + reverse_string + my_string[end:]

    return my_string