inumber = set(range(1,10001))
number = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    number.add(i)

selfnumber = sorted(inumber-number)

for k in selfnumber:
    print(k)
