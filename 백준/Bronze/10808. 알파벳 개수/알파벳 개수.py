x = input()

array = [0]*26

for i in x:
    Index = ord(i)-97
    array[Index]+=1

result =""
for i in array:
    result+= str(i) +" "

print(result.rstrip())
