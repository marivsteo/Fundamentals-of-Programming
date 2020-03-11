'''
Created on 16 Jan 2019
@author: Andreas
'''
auxList1 = []
auxList2 = []

def printStack(stack):
    '''
    This function prints the stack.
    Input: stack, a list of elements
    Output: on-screen
    '''
    stackString = ""
    for el in stack:
        stackString = stackString + " " + str(el)
    print(stackString)    

def increasingOrder(stack):
    '''
    This function checks whether the stack is ordered ascendent.
    Input: stack, a list of elements
    Output: True, if the elements are in increasing order
            False,if the elements are not in increasing order
    '''
    lastel = stack[len(stack)-1]
    currentel = stack[len(stack)-2]
    if lastel <= currentel:
        return False
    return True

def testIO():
    '''
    This function tests whether increasingOrder works properly.
    '''
    list = [10,20,23,45]
    assert increasingOrder(list) == True
    list = [20,10,8,5]
    assert increasingOrder(list) == False

def commonDigits(stack):
    '''
    This function checks whether the elements in the stack have a common digit.
    Input: stack, a list of elements
    Output: True, if all the elements of the stack have one common digit
            False, if all the elements of the stack do not have one common digit
    '''
    lastel = stack[len(stack)-1]
    currentel = stack[len(stack)-2]
    digits = [0]*9

    while lastel != 0:
        digits[int(lastel%10)] += 1
        lastel = int(lastel // 10)
        
    while currentel != 0:
        if digits[int(currentel%10)] != 0:
            return True
        currentel = int(currentel // 10)
    return False

def testCD():
    '''
    This function tests whether commonDigits works properly.
    '''
    list = [10,21,11]
    assert commonDigits(list) == True
    list = [20,10,23,45]
    assert commonDigits(list) == False
    list = [20,10,13,35]
    assert commonDigits(list) == True

def validateStack(stack):
    '''
    This function checks whether the stack meets the required conditions.
    Input: stack, a list of elements
    Output : True, if the stack is valid
             False, if the stack is not valid
    '''
    if len(stack) == 1:
        return True
    if increasingOrder(stack) and commonDigits(stack):
        return True
    return False

def testVS():
    '''
    This function tests whether validateStack works properly.
    '''
    list = [10,21,31]
    assert validateStack(list) == True
    list = [10,21,14]
    assert validateStack(list) == True
    list = [21,18,12]
    assert validateStack(list) == False

def backRec(stack, array):
    '''
    This function solves the problem in a recursive way.
    '''
    if len(stack) == len(array):
        printStack(stack)
    else:
        for el in array:
            stack.append(el)
            if validateStack(stack):
                if len(stack) > 1:
                    printStack(stack)
                backRec(stack, array)
            stack.pop()

def backIter(stack, array):
    '''
    This function solves the problem in an iterative way.
    '''
    cnt = [0]*len(array)
    resList = []
    while True:
        stack = []
        for i in range(len(cnt)):
            if cnt[i] == 1:
                stack.append(array[i])
                if not stack in resList: 
                    if not validateStack(stack):
                        break
                    if len(stack) > 1:
                        auxList2.append(stack)
                        printStack(stack)
                        resList.append(stack)
        
        i = 0
        while i < len(cnt) and cnt[i] == 1:
            cnt[i] = 0
            i+=1
        if i == len(cnt):
            break
        cnt[i]=1

def testBack():
    #print(auxList1)
    #print(auxList2)
    pass

def runTest():
    testIO()
    testCD()
    testBack()

def start():
    stack = []
    array = [11, 25, 10, 84, 24, 65, 88, 23,10,12,45,62]
    array.sort()
    print(array)
    print("Recursive : ")
    backRec(stack, array)
    print("Iterative : ")
    backIter([], array) 

start()
runTest()