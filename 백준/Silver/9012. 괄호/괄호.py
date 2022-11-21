num = int(input())


for i in range(num):
    data = list(input())
    stack_memory = []
    for i in range(len(data)):
        if data[i]=="(":
            stack_memory.append(data[i])
        elif data[i]==")":
            if len(stack_memory) ==0:
                print("NO")
                break
            stack_memory.pop()
       

        if i == len(data)-1 and len(stack_memory) >0:
            print("NO")
            break

        if i == len(data)-1 :
            print("YES")

