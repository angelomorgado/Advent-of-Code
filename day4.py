import numpy as np
import itertools

data = open("input_day4.txt","r")
#data = open("test.txt","r")

#Checks if the dictionary wins
def checkWin(d):
    #turn dict to list
    l = list(d.values())
    
    matrix = np.array(l).reshape(5,5)
    #Check win conditions
    for i in range(5):
        #Check lines
        if matrix[i,:].all() == 1:
            return True
        
        #Check columns
        if matrix[:,i].all() == 1:
            return True
    return False    


def sumAllZeroes(d):
    #Initiates coutn
    count = 0
    #sums every that has 0
    for i in d:
        if d.get(i) == 0:
            count += i
    return count
    

def ex1():
    #Reads the first line of results and stores it in a list (Strip gets rid of the \n)
    results = data.readline().strip().split(',')
    print(results)
    
    #gets rid of annoying space
    space = data.readline()
    
    #Reads the remaining of the file and stores it in a list of matrices
    dictList = []
    for line in data:
        auxDict = {}
        for i in range(5):
            for f in line.strip().split(' '):
                auxDict[int(f)] = 0
                
            line = data.readline()
        dictList.append(auxDict)
    
    
    #Goes through the list and adds the checkmark
    previousNum = -1
    
    for i in results:
        for d in dictList:
            #If the dictionary wins
            if checkWin(d):
                sum = sumAllZeroes(d)
                print(sum ,' * ', previousNum ,'= ', sum*int(previousNum))
                return
            
            #If the key exists in the dictionary
            if int(i) in d:
                d[int(i)] = 1
                
        previousNum = i
    
def ex2():
   #Reads the first line of results and stores it in a list (Strip gets rid of the \n)
    results = data.readline().strip().split(',')
    
    #gets rid of annoying space
    space = data.readline()
    
    #Reads the remaining of the file and stores it in a list of matrices
    dictList = []
    for line in data:
        auxDict = {}
        for i in range(5):
            for f in line.strip().split(' '):
                auxDict[int(f)] = 0
                
            line = data.readline()
        dictList.append(auxDict)
    
    
    #Goes through the list and adds the checkmark
    previousNum = -1
    
    #List of boards that won 
    controlList = []
    
    for i in results:
        for d in dictList:   
            #the last board to win
            if len(controlList) == len(dictList):
                sum = sumAllZeroes(controlList[-1])
                print(sum ,' * ', previousNum ,'= ', sum*int(previousNum))
                return

            if d not in controlList and checkWin(d):
                controlList.append(d)
                continue
            
            #If the key exists in the dictionary
            if d not in controlList and int(i) in d:
                d[int(i)] = 1
            
        previousNum = i          

ex2()