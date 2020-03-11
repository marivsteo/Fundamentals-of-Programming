def is_proper_factor(x,y):
    '''
    The function checks whether x is an factor of y.
    Input : x, an natural number
            y, an natural number
    Preconditions : -
    Output : True, if x is a factor of y.
             False, if x is not a factor of y.
    Postconditions : -
    '''
    if y/x == int(y/x): # If the result of y/x is an integer
        return True     # then x is a factor of y.
    else :
        return False    # otherwise, x is not a factor of y.
    
def read():
    '''
    The function reads and validates the values for x.
    Input : -
    Preconditions : -
    Output : x, an natural number.
    Postconditions : -
    '''
    x = input('Enter a natural number : ')
    try: # We check wheter a string or a number was read.
        x = int(x)
    except: # If it wasn't a number, we re-read.
        x = input('Enter a number not a string : ')
    x = int(x)
    while x < 0:
        x = input('Enter a positive number : ')
    x = int(x) # We convert x into int to be sure of its type.
    return x
        
def ui():
    '''
    This is the main function.
    '''
    a = read() # We read the number.
    p = 1 # We declare and initialize p with one.
          # p will be the result. 
    for i in range( 2,int(a/2)+1): # Then we traverse all the numbers
                            # between 2 and a/2+1
        if( is_proper_factor(i,a) == True ): # If i is a factor of a.
            p *= i # Then we multiply it with p.
    if p == 1: # If p is still 1 then a did not have any proper factors.
        print('The number does not have any proper factors')
    else :
        print(p)
    
ui()
