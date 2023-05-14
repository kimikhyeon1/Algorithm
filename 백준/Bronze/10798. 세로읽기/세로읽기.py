word = []
length = []
for i in range(5):
    x = input()
    word.append(x)
    length.append(len(x))
str = ""
for i in range(max(length)):
    for j in range(5):
        if length[j] > i:
            str+=word[j][i]
print(str)