N = int(input())

pattern = input().split('*')

for _ in range(N):
    inputString = input()
    if inputString[:len(pattern[0])] == pattern[0] and inputString[-len(pattern[-1]):] == pattern[-1] and len("".join(pattern)) <= len(inputString):
        print("DA")
    else:
        print("NE")