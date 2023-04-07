def solution(players, callings):
    rank_dic = {}
    player_dic = {}

    for num,name in enumerate(players):
        rank_dic[num] = name
        player_dic[name] = num

    for name in callings:
        cur_rank = player_dic[name]
        pre_rank = player_dic[name] - 1
        pre_player = rank_dic[pre_rank]

        rank_dic[cur_rank], rank_dic[pre_rank] = rank_dic[pre_rank], rank_dic[cur_rank]
        player_dic[name], player_dic[pre_player] = player_dic[pre_player], player_dic[name]

    return list(rank_dic.values())
