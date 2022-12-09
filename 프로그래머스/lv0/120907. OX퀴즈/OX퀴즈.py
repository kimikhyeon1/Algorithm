def solution(quiz):
    answer = []

    for quizs in quiz:
        split = quizs.split("=")
        if eval(split[0])==int(split[1]):
            answer.append("O")
        else:
            answer.append("X")

    return answer