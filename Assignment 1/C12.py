def read():
     '''
     The function returns a value that is read from the keyboard.
     Input : -
     Preconditions : -
     Output : x, an integer.
     Postconditions : -
     '''
     x = input('Enter a natural number : ')
     while True:
          try: # Here we check that the user has introduced a number
               x = int(x)
               break
          except ValueError as xx:
               print('Enter a number, not a string !')
               x = input('Enter a natural number : ')
     return x

def ui():
     '''
     The function checks whether two number hae the property P.
     Two numbers have the property P if their writings in basis 10 have the same
     digits.
     Input : -
     Preconditions : -
     Output : -
     Postconditions : -
     '''
     print('Enter two numbers to check if they have the property P.')
     print('Give a value for a.')
     a = read()
     a = int(a)
     print('Give a value for b.')
     b = read()
     b = int(b)
     # Now we declare the list where we will memorise for each number which
     # digits appears in their decimal writing. So if figuresOfA[x] is 0, it
     # means that the digit x does not appear in the writing of a. But if it
     # appears, then figuresOfA[x] would be 1.
     figuresOfA = [0,0,0,0,0,0,0,0,0,0]
     figuresOfB = [0,0,0,0,0,0,0,0,0,0]
     # We decompose the first number and we 'mark' each digits' appearance.
     while a > 0:
          figuresOfA[a%10] = 1
          a = a / 10
          a = int(a)
     # We do the same for the second number.
     while b > 0:
          figuresOfB[b%10] = 1
          b = b / 10
          b = int(b)
     
     exit = 0
     # We go trough both the list and if there is a digit in one number that
     # does not appear in the second or vice-versa the for loop will stop
     # because the numbers do not have the property P.
     for x in range(10) :
          if figuresOfA[x] != figuresOfB[x]:
               print('The two numbers do not have the property P.')
               exit = 1
               break
     if( exit == 0 ) :
          print('The two numbers do have the property P.')
          
ui()
