from collections import Counter

f = open("input_day6.txt", "r")
#f = open("test.txt", "r")
data = f.readline().strip()
 
def isUnique(s):
    return len(Counter(s)) == len(s)

def part1():
    total = 0

    for i in range(len(data)):
        s = data[i] + data[i+1] + data[i+2] + data[i+3]
        
        if isUnique(s):
            break
        
        total += 1
        
    print(total + 4) 
    
def part2():
    total = 0

    for i in range(len(data)):
        s = data[i:i+14]
        
        if isUnique(s):
            break
        
        total += 1
    print(s)
        
    print(total + 14) 
      
part1()  
part2() 