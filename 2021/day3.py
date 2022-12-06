import numpy as np

data = [[j for j in i] for i in open('input_day3.txt').read().splitlines()]
numberSize = len(str(data[0]))



#or int('10101',2)
def bitToDecimal(n):
    l = list(reversed(list(map(int, str(n)))))
    count = 0
    n = 0
    for i in range(len(l)):
        if l[i] == 1:
            count += 2**(i)
    
    return count
        

def ex1():
    data1 = [i.strip() for i in open('input_day3.txt').readlines()]
    numberSize = len(str(data1[0]))
    count1List = np.zeros(numberSize)
    
    for i in data:
        for f in range(numberSize):
            if i[f] == '1':
                count1List[f] += 1
    
    Gamma = ""
    Epsilon = ""
    
    for i in count1List:
        if i >= len(data1)/2:
            Gamma = Gamma + '1'
            Epsilon = Epsilon + '0'
        else:
            Gamma = Gamma + '0'
            Epsilon = Epsilon + '1'

                    
    print(bitToDecimal(int(Epsilon)) * bitToDecimal(int(Gamma)))
    


#Ex2
def mostCommon(a,index):
    print(a.T)
    
def leastCommon(a,index):
    count = 1
    if count < len(a)/2:
        return 1
    else:
        return 0
    
        
def getUpdatedList(type, arr, index):
    if type == 1:
        arrAux = []
        if arr.T[index].astype('uint').mean() >= 0.5:
            for i in arr:
                if i[index] == '1':
                    arrAux.append(i)
            arrAux = np.array(arrAux)
            return arrAux
        else:
            for i in arr:
                if i[index] == '0':
                    arrAux.append(i)
            arrAux = np.array(arrAux)
            return arrAux
            
    else:
        arrAux = []
        if arr.T[index].astype('uint').mean() < 0.5:
            for i in arr:
                if i[index] == '1':
                    arrAux.append(i)
            arrAux = np.array(arrAux)
            return arrAux
        else:
            for i in arr:
                if i[index] == '0':
                    arrAux.append(i)
            arrAux = np.array(arrAux)
            return arrAux
        
        
    

def ex2():
    
    O2Value = 0
    Co2Value = 0
    
    O2Arr = np.array(data)
    Co2Arr = np.array(data)
    
    
    for i in range(numberSize):
        
        if len(O2Arr) == 1:
            O2Value = O2Arr[0]
        else:
            O2Arr = getUpdatedList(1, O2Arr, i)
            
        if len(Co2Arr) == 1:
            Co2Value = Co2Arr[0]
        else:
            Co2Arr = getUpdatedList(0, Co2Arr, i)
        

    #most common
    #print(arr)
    print(int("".join(O2Value),2) * int("".join(Co2Value),2))
    
    
        
            
        
#ex1()
ex2()