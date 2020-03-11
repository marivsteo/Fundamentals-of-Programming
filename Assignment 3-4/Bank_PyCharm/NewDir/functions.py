from validate import *

def printIntroduction():
    '''
    The function prints the introduction message to the user.
    '''
    print("This is an app for managing a bank account.")

def saveUndo(trackList,transactionList):
    '''
    This function saves at every step the list before a command is executed.
    Input : trackList, transactionList
    Preconditions : trackList is a list of previous transaction lists
                    transactionList is a list of transactions
    Output :
    Postconditions :
    '''
    auxiliaryList = []
    for x in range(len(transactionList)):
        auxiliaryList.append(transactionList[x])
    trackList.append(auxiliaryList)

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
    day = 31
    value = int(parameters[1])
    type = parameters[2]
    description = parameters[3]
    return {"day": day, "value": value, "type": type, "description": description}

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
    return {"day": day, "value": value, "type": type, "description": description}

def addElementToList(transactionList, newElement):
    '''
    This function appends a new element to the list.
    Input : transactionList, newElement
    Preconditions : transactionList is a list of transactions
                    newElement is a new transaction
    Output :
    Postconditions :
    '''
    transactionList.append(newElement)

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

    if errors == "":
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

def add(transactionList, parameters):
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
        addElementToList(transactionList, newElement)
    else:
        printException(validateAddParameters(parameters))

def insert(transactionList, parameters):
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
        transactionList = addElementToList(transactionList, newElement)
    else:
        printException(validateInsertParameters(parameters))

# ------------------------------- THE WRITE FEATURE STARTS HERE ------------------------------#
def sumOfIn(transactionList, day):
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
        if transactionList[x]["type"] == "in" and transactionList[x]["day"] <= day:
            totalIn = totalIn + transactionList[x]["value"]
    return totalIn

def sumOfOut(transactionList, day):
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
        if transactionList[x]["type"] == "out" and transactionList[x]["day"] <= day:
            totalOut = totalOut + transactionList[x]["value"]
    return totalOut

def determineBalance(transactionList, day):
    '''
    This function computes the balance of the account till the day day.
    Input : transactionList, day
    Preconditions : transactionList is a list of transactions
                    day is an integer
    Output : total
    Postconditions : total is an integer representing the balance.
    '''
    total = sumOfIn(transactionList, day)
    total = total - sumOfOut(transactionList, day)
    return total

def printBalance(total, day):
    '''
    This function prints the balance of transactions occured till the day day.
    Input : total, day
    Preconditions : total, an integer representing the balance
                    day, an integer representing the day of the balance
    Output : on-screen message displaying the balance
    Postconditions :
    '''
    print("The balance till day " + str(day) + " is " + str(total) + ".")

# -------------------------- THE CHARACTERISTICS FEATURE STARTS HERE -------------------------#
def totalSumOfType(transactionList, type):
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
        if transactionList[x]["type"] == type:
            sum = sum + transactionList[x]["value"]
    return sum

def determineMaximumOfType(transactionList, type, day):
    '''
    This function determines the maximum transaction amount of a given type occured in a certain day.
    Input : transactionList, type, day
    Preconditions : transactionList is a list of transaction
                    type is the type of transaction € { in, out }
                    day is the day of the transactions we choose from
    Output : max
    Postconditions : max is the maximum value of a transaction of the given type that occured in the day day
                     -1, if there is no transaction of the specified type in the specified day
    '''
    max = -1
    for x in range(len(transactionList)):
        if transactionList[x]["type"] == type and transactionList[x]["day"] == int(day):
            if transactionList[x]["value"] > max:
                max = transactionList[x]["value"]
    if max == -1:
        return 0
    else:
        return max

# ----------------------------- THE FILTER FEATURE STARTS HERE -----------------------------#
def filterTransactionList(transactionList, type):
    '''
    This function eliminate the transactions which are of the type type from the list of the transactions.
    Input : transactionList, type
    Preconditions : transactionList is a list of
    '''
    filteredList = []
    for x in range(0, len(transactionList)):
        if transactionList[x]["type"] == type:
            filteredList.append(transactionList[x])
    return filteredList

def convertAmount(string):
    try:
        string = int(string)
        return True
    except ValueError as VE:
        return "The amount must be an positive integer."

def filterTransactionList2(transactionList, type, amount):
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
    for x in range(0, len(transactionList)):
        if transactionList[x]["type"] == type and transactionList[x]["value"] < amount:
            filteredList.append(transactionList[x])
    return filteredList

# ----------------------------- THE REMOVE FEATURE STARTS HERE -----------------------------#
def removeDay(transactionList, day):
    '''
    This function removes all the transactions that occured in a specified day.
    Input : transactionList, day
    Preconditions : transactionList is a list of transactions
                    day is the specified day
    Output : transactionList
    Postconditions : transactionList does not contain any transaction that occured in the specified day
    '''
    filteredList = []
    for x in range(0, len(transactionList)):
        if transactionList[x]["day"] != day:
            filteredList.append(transactionList[x])
    transactionList[:] = filteredList

def removeBetween(transactionList, startingPoint, endingPoint):
    for x in range(int(startingPoint) + 1, int(endingPoint)):
        removeDay(transactionList, x)

def findDescription(transactionList, description):
    '''
    This function checks whether in the list of transactions exist a transaction with the given description.
    Input : transactionList, description
    Preconditions : transactionList is a list of transactions
                    description is the specified description that is searched in the transactions
    Output : True, False
    Postconditions : True, if the given description exists in the list of transactions
                     False, if the given description doesn't exist in the list of transactions
    '''
    for x in range(len(transactionList)):
        if transactionList[x]["description"] == description:
            return True
    return False

def replaceDay(transactionList, command):
    '''
    This function replace the amount of  a specified transaction.
    Input : transactionList, command
    Preconditions : transactionList is a list of transactions
                    command is a string which stores the command as a list of strings
    Output : transactionList
    Postonditions : transactionList but with the specified transaction's amount updated
    '''
    for x in range(len(transactionList)):
        if transactionList[x]["description"] == command[3] and transactionList[x]["day"] == int(command[1]) and \
                transactionList[x]["type"] == command[2]:
            transactionList[x]["value"] = int(command[5])