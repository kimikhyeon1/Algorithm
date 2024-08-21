# 윤년이란 2월 29일이 존재 -> 1년이 366일 
# 31 29 31 30 31 30 31 31 30 31 30 31
def solution(a, b):
    month_day_map = { 1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 
                      7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
    day_map = { 1 : "FRI", 2 : "SAT", 3 : "SUN", 
               4 : "MON", 5 : "TUE", 6 : "WED", 0 : "THU"}
    day = b
    
    for i in range(1, a):
        day += month_day_map[i]
    
    return day_map[day % 7] 
