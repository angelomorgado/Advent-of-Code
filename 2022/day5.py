import numpy as np

# Get data
data = [line for line in open('input_day5.txt', 'r')]

def file_to_structure():
    stack_list = np.empty((9, 0)).tolist()
    
    # File to structure
    for line in range(8):
        for char_i in range(1,9*4, 4):
            stack_list[int(char_i / 4)].append(data[line][char_i])
    
    # Invert structure
    for l in range(len(stack_list)):
        stack_list[l] = stack_list[l][::-1]
        
    # Eliminate empty
    for l in range(len(stack_list)):
        stack_list[l] = [value for value in stack_list[l] if value != ' ']
    
    return stack_list
        
def part1():
    stack_list = file_to_structure()
    
    i = 10
    while i != len(data):
        qtt = int(data[i].split(' ')[1])
        origin = int(data[i].split(' ')[3]) - 1
        destination = int(data[i].split(' ')[5]) - 1
        
        for j in range(qtt):
            stack_list[destination].append(stack_list[origin][-1])
            stack_list[origin].pop()  
        i+=1
        
    s = ''
    for j in range(9):
        s += stack_list[j][-1]
    
    print(s)

def part2():
    stack_list = file_to_structure()
    
    i = 10
    while i != len(data):
        qtt = int(data[i].split(' ')[1])
        origin = int(data[i].split(' ')[3]) - 1
        destination = int(data[i].split(' ')[5]) - 1
        
        aux_stack = []
        for j in range(qtt):
            aux_stack.insert(0, stack_list[origin][-1])
            stack_list[origin].pop(-1)  
            
        stack_list[destination] += aux_stack
        
        i+=1
                
    s = ''
    for j in range(9):
        s += stack_list[j][-1]
        
    print(s)    

part1()
part2()