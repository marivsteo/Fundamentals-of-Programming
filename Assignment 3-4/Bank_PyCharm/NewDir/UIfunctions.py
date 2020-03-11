from functions import *

def undoUI(trackList,transactionList):
    '''
    This function creates a list that is appended to the tracklist.
    Input : trackList, transactionList, command
    Preconditions : trackList is a list of previous transaction lists
                    transactionList is a list of transactions
    Output :
    Postconditions :
    '''
    if( len(trackList) != 0 ):
        transactionList[:] = trackList[len(trackList) - 1]
        del trackList[len(trackList)-1]
    else:
        print("There is no more undos to execute.")

def replaceUI(transactionList, command):
    '''
    This function validates the command which was introduced by the user and if it is correct, executes it.
    Input : transactionList, command
    Preconditions : transactionList is a list of transactions
                    command is the command but stored as a list of strings word by word
    Output : on-screen
    Postconditions : message
    '''
    if validateReplace(command) == True and findDescription(transactionList, command[3]) == True and validateDay(
            command[1]) == True:
        replaceDay(transactionList, command)
        print("The replacement was performed.")
    else:
        if findDescription(transactionList, command[3]) != True:
            print("There does not exist a transaction with such a description.")
        if validateDay(command[1]) != True:
            print(validateDay(command[1]))
        if command[2] != "in" and command[2] != "out":
            print("The type of the specified operation must be IN or OUT.")

def removeUI(transactionList, command):
    '''
    This function determines whether the command was introduced correctly and executes it if it was, displays error message otherwise.
    Input : transactionList, command
    Preconditions : transactionList is a list of transactions
                    command is a list of strings containing the command introduced
    Output : on-screen
    Postconditions : message, if the command introduced was not correct
                     -, if the command was executed
    '''
    if len(command) == 2 and (command[1] == "in" or command[1] == "out"):
        removeTypeUI(transactionList, command[1])
    elif len(command) == 2 and validateDay(command[1]) == True:
        removeDay(transactionList, int(command[1]))
    elif len(command) == 4 and command[2] == "to":
        removeBetweenUI(transactionList, command[1], command[3])
    else:
        print("Invalid command. Try again !")

def removeBetweenUI(transactionList, startingPoint, endingPoint):
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
    if validateDay(startingPoint) == True and validateDay(endingPoint) == True:
        removeBetween(transactionList, startingPoint, endingPoint)
    else:
        print("The day must be a positive integer.")

def removeTypeUI(transactionList, type):
    '''
    This function keeps only the transactions that are of the type type.
    Input : transactionList, type
    Preconditions : transactionList is a list of transactions
                    type is the type of the transacctions that will be left
    Output : transactionList
    Postconditions : transactionList only with the transactions of the specified type
    '''
    if type == "in":
        transactionList[:] = filterTransactionList(transactionList, "out")
    else:
        transactionList[:] = filterTransactionList(transactionList, "in")

def filterTypeAmountUI2(transactionList, type, amount):
    '''
    This function removes the transactions that are not of the introduced type and less than the amount value.
    Input : transactionList, type, amount
    Preconditions : transactionList is a list of transactions
                    type is the type of the transactions that will remain
                    amount is the maximum value of the transaction that will remain
    Output :
    Postconditions :
    '''
    transactionList[:] = filterTransactionList2(transactionList, type, amount)

def filterTypeAmountUI(transactionList, command):
    '''
    This function validates whether the amount of the command was introduced correctly.
    Input : transactionList, command
    Preconditions : transactionList is a list of transaction
                    command a string containing a command
    Output :
    Postconditions :
    '''
    if convertAmount(command[2]) == True:
        filterTypeAmountUI2(transactionList, command[1], int(command[2]))
    else:
        print(convertAmount(command[2]))

def filterUI(transactionList, command):
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
            filterTypeUI(transactionList, command[1])
        else:
            filterTypeAmountUI(transactionList, command)

def filterTypeUI(transactionList, type):
    '''
    This function filters the list of transactions eliminating the transaction if the type type.
    Input : transactionList, type
    Precondtitions : transactionList is a list of transactions
                     type is the type of transaction that the users wish to delete
    Output :
    Postconditions :
    '''
    if( type == "in" or type == "out"):
        transactionList[:] = filterTransactionList(transactionList, type)
    else:
        print("Invalid command. Try again !")

def maximumUI(transactionList, type, day):
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
        print(determineMaximumOfType(transactionList, type, day))

def characteristicUI(transactionList, command):
    '''
    This function determines which command the user introduced and executes it.
    Input : transactionList, command
    Preconditions : transactionList is a list of transactions
                    command is a list of strings
    Output : on-screen
    Postconditions : what the user has requested, if the command introduced can be executed
                     error message, if the command was not introduced properly
    '''
    if len(command) == 2 and ( command[1] == "in" or command[1] == "out"):
        print(str(totalSumOfType(transactionList, command[1])))
    elif len(command) == 3 and ( command[1] == "in" or command[1] == "out") and validateDay(command[2]) == True:
        maximumUI(transactionList, command[1], command[2])
    elif len(command) == 1:
        print("Invalid type. Try again specifying the type!")
    else:
        print("Invalid command. Try again !")

def listUI(transactionList, parameters):
    '''
    This functions determines which list command the user has introduced, then executes it.
    Input : transactionList, parameters
    Preconditions : transactionList is a list of transactions
                    parameters a list
    Output : what the user wants.
    Postconditions :
    '''
    if len(parameters) == 1:
        printEntireListUI(transactionList)
    elif parameters[1] == "balance" and validateDay(parameters[2]) == True:
        day = int(parameters[2])
        printBalanceUI(transactionList, day)
    elif parameters[1] == "in" or parameters[1] == "out":
        printTypeListUI(transactionList, parameters[1])
    elif parameters[1] == "<" or parameters[1] == "=" or parameters[1] == ">":
        printAmountListUI(transactionList, parameters)
    else:
        print("Invalid command. Try again !")

def printAmountListUI(transactionList, parameters):
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
        printEqualAmountUI(transactionList, int(parameters[2]))
    elif parameters[1] == "<":
        printLowerAmountUI(transactionList, int(parameters[2]))
    else:
        printGreaterAmountUI(transactionList, int(parameters[2]))

def printEqualAmountUI(transactionList, amount):
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
            print(str(transactionList[x]["day"]) + " " + str(transactionList[x]["value"]) + " " +
                  str(transactionList[x]["type"]) + " " + str(transactionList[x]["description"]))
            printed = True
    if (printed == False):
        print("There are not any transactions with the value equal to " + str(amount) + ".")

def printLowerAmountUI(transactionList, amount):
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
            print(str(transactionList[x]["day"]) + " " + str(transactionList[x]["value"]) + " " +
                  str(transactionList[x]["type"]) + " " + str(transactionList[x]["description"]))
            printed = True
    if (printed == False):
        print("There are not any transactions with the value lower than " + str(amount) + ".")

def printGreaterAmountUI(transactionList, amount):
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
            print(str(transactionList[x]["day"]) + " " + str(transactionList[x]["value"]) + " " +
                  str(transactionList[x]["type"]) + " " + str(transactionList[x]["description"]))
            printed = True
    if (printed == False):
        print("There are not any transactions with the value lower than " + str(amount) + ".")

def printBalanceUI(transactionList, day):
    '''
    This function computes and prints the balance of the account till the day day.
    Input : transactionList, day
    Preconditions : transactionList is a list of transactions
                    day is an integer
    Output :
    Postconditions :
    '''
    total = determineBalance(transactionList, day)
    printBalance(total, day)

def printTypeListUI(transactionList, type):
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
        havePrinted = 0
        print("The list of " + str(type) + " transactions is")
        for x in range(len(transactionList)):
            if transactionList[x]["type"] == type:
                havePrinted = 1
                print(str(transactionList[x]["day"]) + " " + str(transactionList[x]["value"]) + " " +
                      str(transactionList[x]["type"]) + " " + str(transactionList[x]["description"]))

        if havePrinted == 0:
            print("empty.")

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
            print(str(transactionList[x]["day"]) + " " + str(transactionList[x]["value"]) + " " +
                  str(transactionList[x]["type"]) + " " + str(transactionList[x]["description"]))

def addUI(transactionList, parameters):
    '''
    This function adds an element to the list transactionList.
    Input : transactionList, parameters
    Preconditions : transactionList is a list
                    parameters is a list
    Output : transactionList
    Postconditions : transactionList but with one more element
    '''
    if parameters[0] == 'add':
        add(transactionList, parameters)
    if parameters[0] == 'insert':
        insert(transactionList, parameters)