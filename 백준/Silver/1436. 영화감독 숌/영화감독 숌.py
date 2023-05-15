N = int(input())

count = 0
six = 0
while True:
    six +=1
    if "666" in str(six):
        count +=1

    if count==N:
        print(six)
        break