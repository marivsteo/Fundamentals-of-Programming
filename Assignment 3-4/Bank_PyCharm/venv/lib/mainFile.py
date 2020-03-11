from test import *

runTests()

def main():
    printIntroduction()
    transactionList = []
    trackList = []
    while True:
        command = input("Enter command >> ")
        command = command.split(" ")
        if command[0] == "exit":
            return
        elif command[0] == "add" or command[0] == "insert":
            saveUndo(trackList,transactionList)
            addUI(transactionList, command)
        elif command[0] == "list":
            listUI(transactionList, command)
        elif command[0] == "sum" or command[0] == "max":
            characteristicUI(transactionList, command)
        elif command[0] == "filter" and len(command) > 1:
            saveUndo(trackList, transactionList)
            filterUI(transactionList, command)
        elif command[0] == "remove":
            saveUndo(trackList, transactionList)
            removeUI(transactionList, command)
        elif command[0] == "replace":
            saveUndo(trackList, transactionList)
            replaceUI(transactionList, command)
        elif command[0] == "undo":
            undoUI(trackList,transactionList)
        else:
            print("Illegal command. Please enter again !")

main()