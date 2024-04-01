def solution(id_pw, db):
    user_id = id_pw[0]
    user_pw = id_pw[1]
    
    answer = ""
    
    for data in db:
        test_id = data[0]
        test_pw = data[1]
        
        if test_id == user_id:
            if test_pw == user_pw:
                answer = "login"
                return answer
            else:
                answer = "wrong pw"
                return answer
    
    return "fail"  