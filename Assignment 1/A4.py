def read():
    '''
    The function reads the value of x.
    Input : x, an integer
    Preconditions : x must be a natural number
                      => x >= 0
    Output : x, an integer
    Postconditions : -
    '''
    print('Enter the value of x : ')
    x = input()
    while True:
        try :
            x = int(x) # Checking if we can convert it into an integer.
            break      # If yes, we break the while loop.
        except ValueError as xx : # If not, we re-enter the value for x
            x = input('Enter a number, not a string :')
    while x < 0 : # Checking if x is a natural number and
                  # re-enter it until it is.
        print('Enter a natural number !')
        x = input()
        x = int(x)
    return x

def create_largest_number(x):
    '''
    The function determines the largest number that
    can be formed with the figures of x.
    Input : x, an integer
    Preconditions : -
    Output : number, the result
    Postconditions : -
    '''
    figuresList = [0,0,0,0,0,0,0,0,0,0] # We create the list where all the
                     # digits of x will be placed.
    while x > 0 :
        figuresList[x%10] = figuresList[x%10] + 1 # We take the last digit of
                                                  # x and add it to the list.
        x = x / 10 # We then eliminate the last digit.
        x = int(x) # We then reconvert x back to an integer.
    
    number = 0 # number will be the resulted number.
    digit = 9
    while digit != -1 :
        while figuresList[digit] != 0:
            number = number * 10 + digit
            figuresList[digit] = figuresList[digit] - 1
        digit = digit - 1
    return number
    
def ui():
    '''
    The function reads a natural number and finds the largest natural number
    written with the same digits.
    Input : -
    Preconditions : -
    Output : -
    Postconditions : -
    '''
    a = read() # Read the value of the given number.
    x = create_largest_number(a)
    a = str(a)
    print('The largest number that can be written with the same digits as '+ a + ' is :' )
    print(x)

def test_function():
    '''
    The function determines whether the function create_largest_number
    works properly or not.
    Input : -
    Preconditions : -
    Output : -
    Postconditions :
    '''
    assert create_largest_number(234)==432
    assert create_largest_number(22) == 22
    assert create_largest_number(104)==410
     
test_function()
ui()
