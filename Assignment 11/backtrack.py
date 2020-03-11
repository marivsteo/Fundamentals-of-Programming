'''
Created on 16 Jan 2019

@author: Marius
'''

def printStack(stack):
    strStack = ""
    for elem in stack:
        strStack = strStack + " " + str(elem)
    print(strStack)

def checkIncreasing(stack):
    lastelem = stack[len(stack)-1]
    currentelem = stack[len(stack)-2]
    if lastelem <= currentelem:
        return False
    return True

def commonDigits(stack):
    lastelem = stack[len(stack)-1]
    currentelem = stack[len(stack)-2]
    digits = [0]*9

    while lastelem != 0:
        digits[int(lastelem%10)] += 1
        lastelem = int(lastelem // 10)
        
    while currentelem != 0:
        if digits[int(currentelem%10)] != 0:
            return True
        currentelem = int(currentelem // 10)
    return False

def validateStack(stack):
    if len(stack) == 1:
        return True
    if checkIncreasing(stack) and commonDigits(stack):
        return True
    return False

def recBack(stack, sequence):
    if len(stack) == len(sequence):
        printStack(stack)
    else:
        for elem in sequence:
            stack.append(elem)
            if validateStack(stack):
                if len(stack) > 1:
                    printStack(stack)
                recBack(stack, sequence)
            stack.pop()


def iterBack(stack, sequence):
    counter = [0]*len(sequence)
    results = []
    while True:
        stack = []
        for i in range(len(counter)):
            if counter[i] == 1:
                stack.append(sequence[i])
                if not stack in results: 
                    if not validateStack(stack):
                        break
                    if len(stack) > 1:
                        printStack(stack)
                        results.append(stack)
        
        i = 0
        while i < len(counter) and counter[i] == 1:
            counter[i] = 0
            i+=1
        if i == len(counter):
            break
        counter[i]=1
        



def start():
    stack = []
    sequence = [13, 24, 11, 83, 22, 64, 87, 25]
    
    sequence.sort()
    print(sequence)
    print("Recursive backtracking solutions: ")
    recBack(stack, sequence)
    print("Iterative backtracking solutions: ")
    iterBack([], sequence) 


start()