def solution(chicken):
    answer = 0
    while chicken // 10 != 0:
        coupon = chicken // 10
        chicken = chicken % 10 + coupon
        answer += coupon
    
    return answer