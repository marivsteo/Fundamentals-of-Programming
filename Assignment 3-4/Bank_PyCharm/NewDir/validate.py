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

    if errors == "":
        return errors
    else:
        return errors + "Try again !"


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
    if command[2] != "in":
        return False
    if command[4] != "with":
        return False
    try:
        day = int(command[5])
    except ValueError as VE:
        return False
    return True