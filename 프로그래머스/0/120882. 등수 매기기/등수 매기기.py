# 총 점수를 구한다음 hash로 점수 , 순위를 저장한다.
# for문을 통해 해당 점수에 해당하는 순위를 배열에 넣는다.
def solution(score):
    array = []
    for i in score:
        sum_score = 0
        for j in i:
            sum_score += j
        array.append(sum_score)
        
    rating_dic = {}
    rating = 1
    array.sort(reverse = True)
    
    for i in array:
        if i not in rating_dic:
            rating_dic[i] = rating 
        rating += 1
    
    answer = []
    for i in score:
        answer.append(rating_dic[sum(i)])
    return answer