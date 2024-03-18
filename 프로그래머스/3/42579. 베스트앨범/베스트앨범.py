def solution(genres, plays):
    answer = []
    total_playlist = sum_total_plays(genres, plays) # 장르 총합을 정리한 hash
    # [('pop', 3100), ('classic', 1450)]
    plays_index_hash = make_plays_index(plays) # 재생수에 따른 인덱스 저장 hash
    # {500: 0, 600: 1, 150: 2, 800: 3, 2500: 4}
    sorted_playlist_plays = make_sorted_play(genres, plays) # 장르에 따른 plays 목록 정렬한 hash 
    # {'classic': [800, 500, 150], 'pop': [2500, 600]}
    
    for key, value in total_playlist:
        count = 0
        for i in range(2):
            index = sorted_playlist_plays[key][i]
            
            if len(plays_index_hash[index]) > 1:
                answer.append(plays_index_hash[index][count])
                count += 1
                continue
                
            answer.append(plays_index_hash[index][0])
            if len(sorted_playlist_plays[key]) == 1:
                break

    return answer

def make_sorted_play(genres, plays):
    dic = {}
    for i in range(len(genres)):
        if genres[i] in dic.keys():
            dic[genres[i]].append(plays[i])
        else:
            dic[genres[i]] = [plays[i]] 
        
    for k, v in dic.items():
        v.sort(reverse = True) 
    
    print("1", dic)
    return dic

def make_plays_index(plays):
    dic = {}
    for i in range(len(plays)):
        if plays[i] in dic.keys():
            dic[plays[i]].append(i)
            continue
        dic[plays[i]] = [i]
    print("2", dic)    
    return dic

def sum_total_plays(genres, plays):
    dic = {}
    for i in range(len(genres)):
        if genres[i] in dic.keys():
            dic[genres[i]] += plays[i]
        else:
            dic[genres[i]] = plays[i]
    array = sorted(dic.items(), key = lambda x:x[1], reverse = True)
    print("3", array)
    return array
        
        