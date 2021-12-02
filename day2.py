import numpy as np

data = open("input_day2.txt","r")
#data = [i.strip() for i in open('input').readlines()] <-- Ler file

def ex1():
    horizontal = 0
    vertical = 0
    for l in data:
        x,y = l.split()
        
        if x == "forward":
            horizontal += int(y)
        if x == "down":
            vertical += int(y)
        if x == "up":
            vertical -= int(y)
        
    print(horizontal*vertical)
    
def ex2():
    horizontal = 0
    vertical = 0
    aim = 0
    for l in data:
        x,y = l.split()
        
        if x == "forward":
            horizontal += int(y)
            vertical += int(y) * aim
        if x == "down":
            aim += int(y)
        if x == "up":
            aim -= int(y)
        
    print(horizontal*vertical)
    

#ex1()
ex2()