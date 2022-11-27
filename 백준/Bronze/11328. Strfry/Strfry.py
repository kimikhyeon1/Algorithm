n= int(input())

for i in range(n):
    a ,b = map(list,input().split())
    a.sort()
    b.sort()
    if a==b:
        print("Possible")
    else:
        print("Impossible")