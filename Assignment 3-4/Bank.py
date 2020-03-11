def printIntroduction():
    '''
    The function prints the introduction message to the user.
    '''
    print("This is an app for managing a bank account.")

#----------------------------- THE ADD/INSERT FEATURE STARTS HERE -----------------------------#

def createAddElement(parameters):
    '''
    This function creates a transaction out of a list.
    Input : parameters
    Preconditions : parameters is a list
    Output : a transaction
    Postcondition : the transactions has
                        the day equal with the current day
                        the value equal with parameters[1]
                        the type equal with parameters[2]
                        the description equal with parameters[3]
    '''
    day = 10
    value = int(parameters[1])
    type = parameters[2]
    description = parameters[3]
    return { "day" : day, "value" : value, "type" : type, "description" : description }

def createInsertElement(parameters):
    '''
    This function creates a transaction out of a list.
    Input : parameters
    Preconditions : parameters is a list
    Output : a transaction
    Postcondition : the transactions has
                        the day equal with parameters[0]
                        the value equal with parameters[1]
                        the type equal with parameters[2]
                        the description equal with parameters[3]
    '''
    day = int(parameters[1])
    value = int(parameters[2])
    type = parameters[3]
    description = parameters[4]
    return { "day" : day, "value" : value, "type" : type, "description" : description }    

def addElementToList(transactionList,newElement):
    '''
    This function appends a new element to the list.
    Input : transactionList, newElement
    Preconditions : transactionList is a list of transactions
                    newElement is a new transaction
    Output :
    Postconditions :
    '''
    transactionList.append(newElement)

def validateAddParameters(parameters):
    '''
    This function validates whether the a list can be transformed in a proper transaction.
    Input : parameters
    Preconditions : parameters is a list
    Outpout : errors
    Postconditions : errors is empty if there were no exceptions
                            is containing the message for the user indicating the exception
    '''
    errors = ""
    # We validate the value for the transaction
    try:
        value = int(parameters[1])
    except ValueError as ve:
        errors += "The value is not a positive integer.\n"
    # We validate the type of the transaction
    if parameters[2] != "out" and parameters[2] != "in":
        errors += "The type of the operation must be in or out.\n"
    
    if errors == "" :
        return errors
    else:
        return errors + "Try again !"

def validateInsertParameters(parameters):
    '''
    This function validates whether the a list can be transformed in a proper transaction.
    Input : parameters
    Preconditions : parameters is a list
    Outpout : errors
    Postconditions : errors is empty if there were no exceptions
                            is containing the message for the user indicating the exception
    '''
    errors = ""
    # We validate the day for the transaction
    try:
        day = int(parameters[1])
    except ValueError as ve:
        errors += "The day must be a natural number between 1 and 31.\n"
    # We validate the value for the transaction
    try:
        value = int(parameters[2])
    except ValueError as ve:
        errors += "The value is not a positive integer.\n"
    # We validate the type of the transaction
    if parameters[3] != "out" and parameters[3] != "in":
        errors += "The type of the operation must be in or out.\n"
    
    if errors == "" :
        return errors
    else:
        return errors + "Try again !"

def printException(string):
    '''
    The function prints the exceptions that does not allow a command to be executed.
    Input: string
    Preconditions : string is a string
    Output :
    Postconditions:
    '''
    print(str(string))

def add(transactionList,parameters):
    '''
    This function validates and adds an element to the list if its validated.
    Input : transactionList, parameters
    Preconditions : transactionList is a list
                    parameters is a list
    Output :
    Postconditions :
    '''
    if validateAddParameters(parameters) == "":
        newElement = createAddElement(parameters)
        transactionList = addElementToList(transactionList,newElement)
    else:
        printException(validateAddParameters(parameters))

def insert(transactionList,parameters):
    '''
    This function validates and inserts an element to the list if its validated.
    Input : transactionList, parameters
    Preconditions : transactionList is a list
                    parameters is a list
    Output :
    Postconditions :
    '''
    if validateInsertParameters(parameters) == "":
        newElement = createInsertElement(parameters)
        transactionList = addElementToList(transactionList,newElement)
    else:
         printException(validateInsertParameters(parameters))

def addUI(transactionList,parameters):
    '''
    This function adds an element to the list transactionList.
    Input : transactionList, parameters
    Preconditions : transactionList is a list
                    parameters is a list
    Output : transactionList
    Postconditions : transactionList but with one more element
    '''
    if parameters[0] == 'add':
        add(transactionList,parameters)
    if parameters[0] == 'insert':
        insert(transactionList,parameters)
    return transactionList

#------------------------------- THE WRITE FEATURE STARTS HERE ------------------------------#

def printEntireListUI(transactionList):
    '''
    The function prints the transactions.
    Input : transactionList
    Preconditions : transactionList is a list
    Output : on-screen
    Postconditions : the entire list printed element by element, if the list is not empty
                     message, if the list is empty
    '''
    if len(transactionList) == 0:
        print("The list is empty.")
    else: 
        print("The list of transactions is:")
        for x in range(len(transactionList)):
             print(str(transactionList[x]["day"])  + " " + str(transactionList[x]["value"]) + " " +
                      str(transactionList[x]["type"]) + " " + str(transactionList[x]["description"]))

def sumOfIn(transactionList,day):
    '''
    This function computes the sum of all in transactions occured till the day day.
    Input : transactionList, day
    Preconditions : transactionList is a list of transactions
                    day is an integer
    Output : totalIn
    Preconditions : totalIn is an integer representing the sum of all in transactions occured.
    '''
    totalIn = 0
    for x in range(len(transactionList)):
        if transactionList[x]["type"] == "in" and transactionList[x]["day"] <= day :
            totalIn = totalIn + transactionList[x]["value"]
    return totalIn

def sumOfOut(transactionList,day):
    '''
    This function computes the sum of all out transactions occured till the day day.
    Input : transactionList, day
    Preconditions : transactionList is a list of transactions
                    day is an integer
    Output : totalOut
    Preconditions : totalOut is an integer representing the sum of all out transactions occured.
    '''
    totalOut = 0
    for x in range(len(transactionList)):
        if transactionList[x]["type"] == "out" and transactionList[x]["day"] <= day :
            totalOut = totalOut + transactionList[x]["value"]
    return totalOut

def determineBalance(transactionList,day):
    '''
    This function computes the balance of the account till the day day.
    Input : transactionList, day
    Preconditions : transactionList is a list of transactions
                    day is an integer
    Output : total
    Postconditions : total is an integer representing the balance.
    '''
    total = sumOfIn(transactionList,day)
    total = total - sumOfOut(transactionList,day)
    return total

def printBalance(total,day):
    '''
    This function prints the balance of transactions occured till the day day.
    Input : total, day
    Preconditions : total, an integer representing the balance
                    day, an integer representing the day of the balance
    Output : on-screen message displaying the balance
    Postconditions :
    '''
    print("The balance till day " + str(day) + " is " + str(total) + "." )

def printBalanceUI(transactionList,day):
    '''
    This function computes and prints the balance of the account till the day day.
    Input : transactionList, day
    Preconditions : transactionList is a list of transactions
                    day is an integer
    Output :
    Postconditions :
    '''
    total = determineBalance(transactionList,day)
    printBalance(total,day)

def printTypeListUI(transactionList,type):
    '''
    The function prints the transactions of a certain type.
    Input : transactionList, type
    Preconditions : transactionList is a list
                    type is a string
    Output : on-screen
    Postconditions : the entire list of in/out transactions printed element by element, if the list is not empty
                     message, if the list is empty
    '''
    if len(transactionList) == 0:
        print("The list is empty.")
    else:
        print("The list of " + str(type) + " transactions is:")
        for x in range(len(transactionList)):
            if transactionList[x]["type"] == type:
                print(str(transactionList[x]["day"])  + " " + str(transactionList[x]["value"]) + " " +
                      str(transactionList[x]["type"]) + " " + str(transactionList[x]["description"]))

def printEqualAmountUI(transactionList,amount):
    '''
    This function prints the transaction that have the value equal with amount.
    Input : transactionList, amount
    Preconditions : transactionList is a list of transactions
                    amount is a integer
    Output : on-screen
    Postconditions : the list of the transactions that have the value equal with amount, if there is at least one
                     message, if there is not one
    '''
    printed = False
    for x in range(len(transactionList)):
        if transactionList[x]["value"] == amount:
            print(str(transactionList[x]["day"])  + " " + str(transactionList[x]["value"]) + " " +
                      str(transactionList[x]["type"]) + " " + str(transactionList[x]["description"]))
            printed = True
    if( printed == False ):
        print("There are not any transactions with the value equal to " + str(amount) + ".")

def printLowerAmountUI(transactionList,amount):
    '''
    This function prints the transaction that have the value lower than amount.
    Input : transactionList, amount
    Preconditions : transactionList is a list of transactions
                    amount is a integer
    Output : on-screen
    Postconditions : the list of the transactions that have the value lower than amount, if there is at least one
                     message, if there is not one
    '''
    printed = False
    for x in range(len(transactionList)):
        if transactionList[x]["value"] < amount:
            print(str(transactionList[x]["day"])  + " " + str(transactionList[x]["value"]) + " " +
                      str(transactionList[x]["type"]) + " " + str(transactionList[x]["description"]))
            printed = True
    if( printed == False ):
        print("There are not any transactions with the value lower than " + str(amount) + ".")

def printGreaterAmountUI(transactionList,amount):
    '''
    This function prints the transaction that have the value greater than amount.
    Input : transactionList, amount
    Preconditions : transactionList is a list of transactions
                    amount is a integer
    Output : on-screen
    Postconditions : the list of the transactions that have the value greater than amount, if there is at least one
                     message, if there is not one
    '''
    printed = False
    for x in range(len(transactionList)):
        if transactionList[x]["value"] > amount:
            print(str(transactionList[x]["day"])  + " " + str(transactionList[x]["value"]) + " " +
                      str(transactionList[x]["type"]) + " " + str(transactionList[x]["description"]))
            printed = True
    if( printed == False ):
        print("There are not any transactions with the value lower than " + str(amount) + ".")

def printAmountListUI(transactionList,parameters):
    '''
    This function prints all the transactions that are either greater, equal or lower than the number introduced by the user.
    Input : transactionList, parameters
    Preconditions : transactionList is a list of transactions
                    parameters a list containing the command
    Output : on-screen
    Postconditions : the lisst of items fulfilling a comparison.
    '''
    if len(transactionList) == 0:
        print("The list is empty.")
    elif parameters[1] == "=":
        printEqualAmountUI(transactionList,int(parameters[2]))
    elif parameters[1] == "<":
        printLowerAmountUI(transactionList,int(parameters[2]))
    else:
        printGreaterAmountUI(transactionList,int(parameters[2]))

def listUI(transactionList,parameters):
    '''
    This functions determines which list command the user has introduced, then executes it.
    Input : transactionList, parameters
    Preconditions : transactionList is a list of transactions
                    parameters a list
    Output : what the user wants.
    Postconditions :
    '''
    if len(parameters) == 1 :
        printEntireListUI(transactionList)
    elif parameters[1] == "balance" :
        day = int(parameters[2])
        printBalanceUI(transactionList,day)
    elif parameters[1] == "in" or parameters[1] == "out":
        printTypeListUI(transactionList,parameters[1])
    else:
        printAmountListUI(transactionList,parameters)

#-------------------------- THE CHARACTERISTICS FEATURE STARTS HERE -------------------------#

def totalSumOfType(transactionList,type):
    '''
    This function determines the total sum of all transactions of a certain type.
    Input : transactionList, type
    Preconditions : transactionList is a list of transaction
                    type is a string € {"in","out"}
    Output : sum
    Postconditions : sum is the sum of all transactions of the type type
    '''
    sum = 0
    for x in range(len(transactionList)):
        if transactionList[x]["type"] == type :
            sum = sum + transactionList[x]["value"]
    return sum

def validateDay(string):
    '''
    This functions check whether the user had typed the command correctly.
    Input : string
    Preconditions : string is a string containing a day of a transaction
    Output : True, string
    Postconditions : True, if the day was correctly inputted
                     message, if the day was not a positive integer
    '''
    try:
        string = int(string)
        return True
    except ValueError as VE:
        return "The day must be an positive integer."

def determineMaximumOfType(transactionList,type,day):
    '''
    This function determines the maximum transaction amount of a given type occured in a certain day.
    Input : transactionList, type, day
    Preconditions : transactionList is a list of transaction
                    type is the type of transaction € { in, out }
                    day is the day of the transactions we choose from
    Output : max
    Postconditions : max is the maximum value of a transaction of the given type that occured in the day day
    '''
    max = -1
    for x in range(len(transactionList)):
        if transactionList[x]["type"] == type and transactionList[x]["day"] == int(day):
            if transactionList[x]["value"] > max :
                max = transactionList[x]["value"]
    return max

def maximumUI(transactionList,type,day):
    '''
    This function validates and executes the max command.
    Input : transactionList, type, day
    Preconditions : transactionList is a list of transaction
                    type is the type of transaction € { in, out }
                    day is the day of the transactions we choose from
    Output : on-screen
    Postconditions : error message, if the input data is not viable
                     the maximum if it is viable
    '''
    if validateDay(day) != True:
        print(validateDay(day))
    else:
        print(determineMaximumOfType(transactionList,type,day))

def characteristicUI(transactionList,command):
    '''
    This function determines which command the user introduced and executes it.
    Input : transactionList, command
    Preconditions : transactionList is a list of transactions
                    command is a list of strings
    Output : on-screen
    Postconditions : what the user has requested, if the command introduced can be executed
                     error message, if the command was not introduced properly
    '''
    if len(command) == 2 :
        print(str(totalSumOfType(transactionList,command[1])))
    else:
        maximumUI(transactionList,command[1],command[2])
        
#----------------------------- THE FILTER FEATURE STARTS HERE -----------------------------#
        
def filterTransactionList(transactionList,type):
    '''
    This function eliminate the transactions which are of the type type from the list of the transactions.
    Input : transactionList, type
    Preconditions : transactionList is a list of
    '''
    filteredList = []
    for x in range(0,len(transactionList)):
        if transactionList[x]["type"] == type:
            filteredList.append(transactionList[x])
    return filteredList
            

def filterTypeUI(transactionList,type):
    '''
    This function filters the list of transactions eliminating the transaction if the type type.
    Input : transactionList, type
    Precondtitions : transactionList is a list of transactions
                     type is the type of transaction that the users wish to delete
    Output :
    Postconditions :
    '''
    transactionList[:] = filterTransactionList(transactionList,type)
        
def validateType(string):
    '''
    This function determines whether the command was introduced correctly.
    Input : string
    Preconditions : string is a string
    Output : True, message
    Postconditions : True, if the command was introduced correctly
                     message, if it was not
    '''
    if string == "in" or string == "out":
        return True
    return "The transaction type must be in or out."

def convertAmount(string):
    try:
        string = int(string)
        return True
    except ValueError as VE:
        return "The amount must be an positive integer."

def filterTransactionList2(transactionList,type,amount):
    '''
    This function eliminate the transactions which are of the type type and the value less than amount from the list of the transactions.
    Input : transactionList, type, amount
    Preconditions : transactionList is a list of transactions
                    type is the type of the transactions that will be removed
                    amount is the maximum value of the transactions that will remain
    Output : filteredList
    Postconditions : the list of transaction that are not of the type type and have the value equal with amount
    '''
    filteredList = []
    for x in range(0,len(transactionList)):
        if transactionList[x]["type"] == type and transactionList[x]["value"] < amount:
            filteredList.append(transactionList[x])
    return filteredList

def filterTypeAmountUI2(transactionList,type,amount):
    '''
    This function removes the transactions that are not of the introduced type and less than the amount value.
    Input : transactionList, type, amount
    Preconditions : transactionList is a list of transactions
                    type is the type of the transactions that will remain
                    amount is the maximum value of the transaction that will remain
    Output :
    Postconditions :
    '''
    transactionList[:] = filterTransactionList2(transactionList,type,amount)

def filterTypeAmountUI(transactionList,command):
    '''
    This function validates whether the amount of the command was introduced correctly.
    Input : transactionList, command
    Preconditions : transactionList is a list of transaction
                    command a string containing a command
    Output :
    Postconditions :
    '''
    if convertAmount(command[2]) == True:
        filterTypeAmountUI2(transactionList,command[1],int(command[2]))
    else:
        print(convertAmount(command[2]))

def filterUI(transactionList,command):
    '''
    This function validates the command and executes it.
    Input : transactionList, command
    Preconditions : transactionList is a list of transaction
                    command is a list of string containing the command
    Output :
    Postconditions :
    '''
    if validateType(command[1]) != True:
        print(validateType(command[1]))
    else:
        if len(command) == 2:
            filterTypeUI(transactionList,command[1])
        else:
            filterTypeAmountUI(transactionList,command)

#----------------------------- THE REMOVE FEATURE STARTS HERE -----------------------------#

def removeTypeUI(transactionList,type):
    '''
    This function keeps only the transactions that are of the type type.
    Input : transactionList, type
    Preconditions : transactionList is a list of transactions
                    type is the type of the transacctions that will be left
    Output : transactionList
    Postconditions : transactionList only with the transactions of the specified type
    '''
    if type == "in":
        transactionList[:] = filterTransactionList(transactionList,"out")
    else:
        transactionList[:] = filterTransactionList(transactionList,"in")

def removeDay(transactionList,day):
    '''
    This function removes all the transactions that occured in a specified day.
    Input : transactionList, day
    Preconditions : transactionList is a list of transactions
                    day is the specified day
    Output : transactionList
    Postconditions : transactionList does not contain any transaction that occured in the specified day
    '''
    filteredList = []
    for x in range(0,len(transactionList)):
        if transactionList[x]["day"] != day :
            filteredList.append(transactionList[x])
    transactionList[:] = filteredList

def removeBetween(transactionList,startingPoint,endingPoint):
    for x in range(int(startingPoint)+1,int(endingPoint)):
            removeDay(transactionList,x)

def removeBetweenUI(transactionList,startingPoint,endingPoint):
    '''
    This function validates whether the command was introduced correctly.
    Input : transactionList, startingPoint, endingPoint
    Preconditions : transactionList is a list of transactions
                    startingPoint is a string containing the day from which all later transactions will be deleted
                    endingPoint is a string containing the last day of the transactions that will be deleted
    Output : on_screnn
    Postconditions : message if the command was not introduced correctly
                     -, if the command was successfully executed
    '''
    if validateDay(startingPoint) == True and validateDay(endingPoint) == True :
        removeBetween(transactionList,startingPoint,endingPoint)
    else:
        print("The day must be a positive integer.")

def removeUI(transactionList,command):
    '''
    This function determines whether the command was introduced correctly and executes it if it was, displays error message otherwise.
    Input : transactionList, command
    Preconditions : transactionList is a list of transactions
                    command is a list of strings containing the command introduced
    Output : on-screen
    Postconditions : message, if the command introduced was not correct
                     -, if the command was executed
    '''
    if len(command) == 2 and ( command[1] == "in" or command[1] == "out" ):
        removeTypeUI(transactionList,command[1])
    elif len(command) == 2 and ( command[1] > "0" and command[1] < "999" ):
        removeDay(transactionList,int(command[1]))
    elif len(command) == 4 and command[2] == "to" :
        removeBetweenUI(transactionList,command[1],command[3])

def validateReplace(command):
    '''
    This function checks whether the replace command was introduced properly by the user.
    Input : command
    Preconditions : command is a list of strings containing the command introduced
    Output : True, False
    Postconditions : True, if the command was correctly introduced
                     False, if the command was not correctyle introduced
    '''
    try:
        day = int(command[1])
    except ValueError as VE:
        return False
    if command[2] != "in" :
        return False
    if command[4] != "with" :
        return False
    try:
        day = int(command[5])
    except ValueError as VE:
        return False
    return True

def findDescription(transactionList,description):
    '''
    This function checks whether in the list of transactions exist a transaction with the given description.
    Input : transactionList, description
    Preconditions : transactionList is a list of transactions
                    description is the specified description that is searched in the transactions
    Output : True, False
    Postconditions : True, if the given description exists in the list of transactions
                     False, if the given description doesn't exist in the list of transactions
    '''
    for x in range (len(transactionList)):
        if transactionList[x]["description"] == description:
            return True
    return False

def replaceDay(transactionList,command):
    '''
    This function replace the amount of  a specified transaction.
    Input : transactionList, command
    Preconditions : transactionList is a list of transactions
                    command is a string which stores the commands
    '''
    for x in range (len(transactionList)):
        if transactionList[x]["description"] == command[3] and transactionList[x]["day"] == int(command[1]) and transactionList[x]["type"] == command[2]:
            transactionList[x]["value"] = int(command[5])

def replaceUI(transactionList,command):
    if validateReplace(command) == True and findDescription(transactionList,command[3]) == True and validateDay(command[1]) == True:
        replaceDay(transactionList,command)
    else :
        if findDescription(transactionList,command[3]) != True:
            print("There does not exist a transaction with such a description.")
        if validateDay(command[1]) != True :
            print(validateDay(command[1]))

#------------------------------------------------------------------------------------------#
#----------------------------| THE TEST FUNCTIONS START HERE |-----------------------------#
#------------------------------------------------------------------------------------------#

def testFilterTransactionList2():
    testList = []
    testParameters = ["insert",15,712,"in","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    testParameters = ["insert",15,702,"in","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    testList = filterTransactionList2(testList,"in",710)
    assert testList == [element]
    testList = []
    testParameters = ["insert",15,712,"out","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    testParameters = ["insert",15,702,"in","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    testList = filterTransactionList2(testList,"out",710)
    assert testList == []

def testConvertAmount():
    assert convertAmount("2323") == True
    assert convertAmount("asdas") == "The amount must be an positive integer."

def testValidateType():
    assert validateType("in") == True
    assert validateType("out") == True
    assert validateType("asdas") == "The transaction type must be in or out."

def testFilterTransactionList():
    testList = []
    testParameters = ["insert",15,712,"in","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    testParameters = ["insert",15,722,"out","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    testList = filterTransactionList(testList,"out")
    assert testList == [element]
    testList = []
    testParameters = ["insert",15,722,"out","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    testParameters = ["insert",15,712,"in","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    testList = filterTransactionList(testList,"in")
    assert testList == [element]

def testValidateType():
    assert validateType("in") == True
    assert validateType("out") == True
    assert validateType("outd") == "The transaction type must be in or out."

def filterTests():
    testValidateType()
    testFilterTransactionList()
    testValidateType()
    testConvertAmount()
    testFilterTransactionList2()

def testTotalSumOfType():
    testList = []
    testParameters = ["insert",15,8,"in","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    testParameters = ["insert",15,1,"in","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    testParameters = ["insert",15,3,"in","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    assert totalSumOfType(testList,"in") == 12

def characteristicTests():
    testTotalSumOfType()

def testCreateAddElement():
    testParameters = ["add",712,"in","pizza"]
    element = createAddElement(testParameters)
    assert element == { "day" : 10, "value" : testParameters[1],
                        "type" : testParameters[2], "description" : testParameters[3] }

def testCreateInsertElement():
    testParameters = ["insert",10,69,"in","pizza"]
    element = createInsertElement(testParameters)
    assert element == { "day" : testParameters[1], "value" : testParameters[2],
                        "type" : testParameters[3], "description" : testParameters[4] }

def testAddElementToList():
    testList = []
    testParameters = ["add",712,"in","pizza"]
    element = createAddElement(testParameters)
    addElementToList(testList,element)
    assert testList == [element]
    assert len(testList) == 1

def testValidateAddParameters():
    testParameters = ["add","asda","cheche","pizza"]
    assert validateAddParameters(testParameters) == "The value is not a positive integer.\nThe type of the operation must be in or out.\nTry again !"

def testValidateInsertParameters():
    testParameters = ["insert",10,"asda","23ds","pizza"]
    assert validateInsertParameters(testParameters) == "The value is not a positive integer.\nThe type of the operation must be in or out.\nTry again !"

def testAdd():
    testList = []
    testParameters = ["add",712,"in","pizza"]
    element = createAddElement(testParameters)
    add(testList,testParameters)
    assert testList == [element]

def testInsert():
    testList = []
    testParameters = ["insert",10,252,"in","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    assert testList == [element]

def runAddAndInsertTests():
    testCreateAddElement()
    testCreateInsertElement()
    testAddElementToList()
    testValidateAddParameters()
    testValidateInsertParameters()
    testAdd()
    testInsert()

def testSumOfIn():
    testList = []
    testParameters = ["insert",15,712,"in","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    testParameters = ["insert",15,722,"out","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    assert sumOfIn(testList,16) == 712

def testSumOfOut():
    testList = []
    testParameters = ["insert",15,712,"in","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    testParameters = ["insert",15,722,"out","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    assert sumOfOut(testList,15) == 722

def testDetermineBalance():
    testList = []
    testParameters = ["insert",15,712,"in","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    testParameters = ["insert",15,722,"out","pizza"]
    element = createInsertElement(testParameters)
    insert(testList,testParameters)
    assert determineBalance(testList,15) == -10

def writeTests():
    testSumOfIn()
    testSumOfOut()
    testDetermineBalance()

def runTests():
    runAddAndInsertTests()
    writeTests()
    characteristicTests()
    filterTests()
     
#------------------------------------------------------------------------------------------#
#----------------------------| THE TEST FUNCTIONS  END  HERE |-----------------------------#
#------------------------------------------------------------------------------------------#

runTests()

def main():
    printIntroduction()
    transactionList = []
    while True:
        command = input("Enter command >> ")
        command = command.split(" ")
        if command[0] == "exit":
            return
        elif command[0] == "add" or command[0] == "insert" :
            addUI(transactionList,command)
        elif command[0] == "list" :
            listUI(transactionList,command)
        elif command[0] == "sum" or command[0] == "max" :
            characteristicUI(transactionList,command)
        elif command[0] == "filter":
            filterUI(transactionList,command)
        elif command[0] == "remove":
            removeUI(transactionList,command)
        elif command[0] == "replace":
            replaceUI(transactionList,command)
        else:
            print("Illegal command. Please enter again !")

main()
