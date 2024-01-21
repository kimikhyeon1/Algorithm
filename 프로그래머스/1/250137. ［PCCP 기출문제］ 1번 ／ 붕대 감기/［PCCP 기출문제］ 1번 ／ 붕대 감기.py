# 1. 시전시간, 초 회복량, 추가 회복량 변수를 생성한다.
# 2. for문을 통해 attack의 길이만큼 순회하고 종료되었을때 
#    health 값이 0이하면 -1 리턴 or health 값을 리턴한다. 

def solution(bandage, health, attacks):
    answer = 0
    time = 0
    heel_time = 0
    
    default_health = health

    for array in attacks:
        damage_time = 0
        damage = 0
        for index,element in enumerate(array):
            if index == 0:
                damage_time = element
            else:
                damage = element

            
        while True:
            time += 1
            heel_time +=1
                
            if time == damage_time:
                health -= damage
                heel_time = 0
                break
            else:
                if heel_time == bandage[0]:
                    health += bandage[2]
                    heel_time = 0
                
                health += bandage[1]
                        
                if health > default_health:
                    health = default_health
            
        if health < 1: 
            return -1
    
    return health