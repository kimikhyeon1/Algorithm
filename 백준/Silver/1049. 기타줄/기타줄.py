N , M= map(int,input().split())
most_set, most_one_set = map(int,input().split())
for i in range(M-1):
    six_set1, one_set1 = map(int,input().split())
    if six_set1 < most_set :
        most_set = six_set1
    if one_set1 < most_one_set :
        most_one_set = one_set1
cost = 0
if most_set >most_one_set*6:
    print(N*most_one_set)
elif most_set <= most_one_set*6:
    if N >=6 :
        cost+= N//6*most_set
        N = N%6
        if most_set < N*most_one_set:
            cost +=most_set
        else: cost +=N*most_one_set
        print(cost)
    elif N<6:
        if most_set > N*most_one_set:
            print(N*most_one_set)
        else: print(most_set)