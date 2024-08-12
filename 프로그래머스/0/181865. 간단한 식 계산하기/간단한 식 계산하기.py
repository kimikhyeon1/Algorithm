def solution(binomial):
    array = binomial.split(" ")
    if array[1] == "+":
        return int(array[0]) + int(array[2])
    elif array[1] == "-":
        return int(array[0]) - int(array[2])
    else:
        return int(array[0]) * int(array[2])