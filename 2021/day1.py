f = open("input_day1.txt","r")

def ex1():
    count = 0
    list = []
    for l in f:
        list.append(int(l))
        
    for i in range(len(list)- 3):
        if list[i+1] > list[i]:
            count+=1

    print(count)

def ex2():
    count = 0
    list = []
    for l in f:
        list.append(int(l))
        
    for i in range(len(list)- 3):
        if list[i+1] + list[i+2] + list[i+3] > list[i] + list[i+1] + list[i+2]:
            count+=1

    print(count)
    
#ex1()
ex2()