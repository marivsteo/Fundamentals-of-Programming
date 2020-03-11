from UIfunctions import *
# ------------------------------------------------------------------------------------------#
# ----------------------------| THE TEST FUNCTIONS START HERE |-----------------------------#
# ------------------------------------------------------------------------------------------#

def testFilterTransactionList2():
    testList = []
    testParameters = ["insert", 15, 712, "in", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    testParameters = ["insert", 15, 702, "in", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    testList = filterTransactionList2(testList, "in", 710)
    assert testList == [element]
    testList = []
    testParameters = ["insert", 15, 712, "out", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    testParameters = ["insert", 15, 702, "in", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    testList = filterTransactionList2(testList, "out", 710)
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
    testParameters = ["insert", 15, 712, "in", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    testParameters = ["insert", 15, 722, "out", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    testList = filterTransactionList(testList, "out")
    assert testList == [element]
    testList = []
    testParameters = ["insert", 15, 722, "out", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    testParameters = ["insert", 15, 712, "in", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    testList = filterTransactionList(testList, "in")
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
    testParameters = ["insert", 15, 8, "in", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    testParameters = ["insert", 15, 1, "in", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    testParameters = ["insert", 15, 3, "in", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    assert totalSumOfType(testList, "in") == 12


def characteristicTests():
    testTotalSumOfType()


def testCreateAddElement():
    testParameters = ["add", 712, "in", "pizza"]
    element = createAddElement(testParameters)
    assert element == {"day": 31, "value": testParameters[1],
                       "type": testParameters[2], "description": testParameters[3]}


def testCreateInsertElement():
    testParameters = ["insert", 10, 69, "in", "pizza"]
    element = createInsertElement(testParameters)
    assert element == {"day": testParameters[1], "value": testParameters[2],
                       "type": testParameters[3], "description": testParameters[4]}


def testAddElementToList():
    testList = []
    testParameters = ["add", 712, "in", "pizza"]
    element = createAddElement(testParameters)
    addElementToList(testList, element)
    assert testList == [element]
    assert len(testList) == 1


def testValidateAddParameters():
    testParameters = ["add", "asda", "cheche", "pizza"]
    assert validateAddParameters(
        testParameters) == "The value is not a positive integer.\nThe type of the operation must be in or out.\nTry again !"


def testValidateInsertParameters():
    testParameters = ["insert", 10, "asda", "23ds", "pizza"]
    assert validateInsertParameters(
        testParameters) == "The value is not a positive integer.\nThe type of the operation must be in or out.\nTry again !"


def testAdd():
    testList = []
    testParameters = ["add", 712, "in", "pizza"]
    element = createAddElement(testParameters)
    add(testList, testParameters)
    assert testList == [element]


def testInsert():
    testList = []
    testParameters = ["insert", 10, 252, "in", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
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
    testParameters = ["insert", 15, 712, "in", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    testParameters = ["insert", 15, 722, "out", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    assert sumOfIn(testList, 16) == 712


def testSumOfOut():
    testList = []
    testParameters = ["insert", 15, 712, "in", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    testParameters = ["insert", 15, 722, "out", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    assert sumOfOut(testList, 15) == 722


def testDetermineBalance():
    testList = []
    testParameters = ["insert", 15, 712, "in", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    testParameters = ["insert", 15, 722, "out", "pizza"]
    element = createInsertElement(testParameters)
    insert(testList, testParameters)
    assert determineBalance(testList, 15) == -10


def writeTests():
    testSumOfIn()
    testSumOfOut()
    testDetermineBalance()

def undoTest():
    undoList = []
    testList = []
    testParameters = ["insert", 15, 712, "in", "pizza"]
    insert(testList, testParameters)
    saveUndo(undoList,testList)
    testParameters = ["insert", 15, 722, "out", "pizza"]
    insert(testList, testParameters)
    saveUndo(undoList,testList)
    testParameters = ["insert", 15, 712, "in", "pizza"]
    element = createInsertElement(testParameters)
    undoUI(undoList,testList)
    undoUI(undoList,testList)
    assert testList == [element]



def runTests():
    runAddAndInsertTests()
    writeTests()
    characteristicTests()
    filterTests()
    undoTest()

# ------------------------------------------------------------------------------------------#
# ----------------------------| THE TEST FUNCTIONS  END  HERE |-----------------------------#
# ------------------------------------------------------------------------------------------#