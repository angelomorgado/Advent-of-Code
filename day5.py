import numpy as np

#data = open("test.txt","r")
data = open("input_day5.txt","r")


def addToMatrix(lineMatrix, p):
    
    #So that the for executes flawlessly
    if p[0] > p[2]:
        controlX = -1
    else:
        controlX = 1
    
    if p[1] > p[3]:
        controlY = -1
    else:
        controlY = 1
    
        
        
    #Verify if it's only vertical or horizontal
    #If it's vertical (y)
    if p[0] == p[2]:
        for i in range(p[1], p[3] + controlY,controlY):
            lineMatrix[i][p[0]] += 1
        return lineMatrix
    
    #If it's horizontal
    if p[1] == p[3]:
        for i in range(p[0], p[2] + controlX,controlX):
            lineMatrix[p[1]][i] += 1
        return lineMatrix
    
    #If it's diagonal (exercise 2 comment if you want part 1)
    if p[0] - p[1] == p[2] - p[3] or p[0] + p[1] == p[2] + p[3]:
        
        #x and y smaller
        if p[0] < p[2] and p[1] < p[3]:
            controlDx = 1
            controlDy = 1
        #x bigger , y smaller
        if p[0] > p[2] and p[1] < p[3]:
            controlDx = -1
            controlDy = 1
        #x smaller , y bigger
        if p[0] < p[2] and p[1] > p[3]:
            controlDx = 1
            controlDy = -1
        #x and y bigger
        if p[0] > p[2] and p[1] > p[3]:
            controlDx = -1
            controlDy = -1
        
        x = p[0]
        y = p[1]
        
        for i in range((p[2] - p[0]) * controlDx + 1):
            lineMatrix[y][x] += 1
            x += controlDx
            y += controlDy     
        return lineMatrix
    
    return lineMatrix
    

def ex1():
    
    lineList = []
    lineMatrix = np.zeros(1000000).reshape(1000,1000) 
    for l in data:
        #Organize the data
        x1y1,x2y2 = l.strip().split(" -> ")
        x1,y1 = x1y1.split(",")
        x2,y2 = x2y2.split(",")
        #lineList.append([int(x1),int(y1),int(x2),int(y2)])
        lineMatrix = addToMatrix(lineMatrix, [int(x1),int(y1),int(x2),int(y2)])
    
    
    print(lineMatrix)  
    
    count = 0  
    for i in lineMatrix:
        for f in i:
            if f > 1:
                count += 1
    
    print('count = ',count)


ex1()