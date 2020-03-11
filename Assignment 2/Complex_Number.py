import math

def create_complex_number(a, b ):
    '''
    Function that creates a complex number c given its real part a and imaginary part b.
    c = a + ib with a, b € R.
    Input : a, b
    Preconditions : a, b - are float
    Output : c
    Postconditions : c - complex number
                        the real part of c = a
                        the imaginary part of c = b
    '''
    return {
            "re":a,
            "im":b
            }

def get_Real(c):
    '''
    The function return the real part of the complex number c.
    Input : c
    Preconditions : c - complex number
    Output : r
    Postconditions : r - float, the real part of c
    '''
    return c["re"]

def get_Imag(c):
    '''
    The function return the imaginary part of the complex number c.
    Input : c
    Preconditions : c - complex number
    Output : i
    Postconditions : i - float, the imaginary part of c
    '''
    return c["im"] 

def set_Real(c, x):
    '''
    The function sets the value of the real part of the complex number c at x.
    Input : c, x
    Preconditions : c - a complex number
                    x - a float
    Output : c
    Postconditions : c - complex number with the real part equal with x.
    '''
    c["re"] = x
    return c

def set_Imag(c, x):
    '''
    The function sets the value of the imaginary part of the complex number c at x.
    Input : c, x
    Preconditions : c - a complex number
                    x - a float
    Output : c
    Postconditions : c - complex number with the imaginary part equal with x.
    '''
    c["im"] = x
    return c

def toStr(c):
    '''
    The function writes a complex number like : a + ib, if b > 0
                                                a - ib, if b < 0
    '''
    if get_Imag(c) >= 0 :
        return ( str(c["re"]) + ' + ' + str( c["im"]) + "i" )
    else:
        return ( str(c["re"]) + ' - ' + str(-c["im"]) + "i" )
        
def add_number_to_list(list,c):
    '''
    The function adds the complex number c to the list.
    Input : list, c
    Preconditions : list - a list containing complex numbers
                    c - a complex number
    Output : list
    Postconditions : list contains c at the end
    '''
    list.append(c)
    return list

def initialize_list(listComplex):
    '''
    This function initialises the listComplex list with some complex values.
    Input : listComplex
    Preconditions : listComplex - a empty list
    Output : listComplex
    Postconditions : listComplex will now have 10 complex numbers in it.
    '''
    a = create_complex_number(3.21,-4.90)
    listComplex = add_number_to_list(listComplex, a )
    a = create_complex_number(3.21,1.67)
    listComplex = add_number_to_list(listComplex, a )
    a = create_complex_number(-0.21,-9.90)
    listComplex = add_number_to_list(listComplex, a )
    a = create_complex_number(0,0)
    listComplex = add_number_to_list(listComplex, a )
    a = create_complex_number(0.01,-24.90)
    listComplex = add_number_to_list(listComplex, a )
    a = create_complex_number(3,-4)
    listComplex = add_number_to_list(listComplex, a )
    a = create_complex_number(2,1)
    listComplex = add_number_to_list(listComplex, a )
    a = create_complex_number(-6,-3)
    listComplex = add_number_to_list(listComplex, a )
    a = create_complex_number(3.21,0)
    listComplex = add_number_to_list(listComplex, a )
    a = create_complex_number(0,-4.9)
    listComplex = add_number_to_list(listComplex, a )
    return listComplex

def print_number_of_elements(nmb):
    '''
    The function determines and prints how many elements does list have.
    Input : nmb
    Preconditions : nbm - number of elements of a list
    Output :
    Postconditions :
    '''
    print()
    print('The list has ' + str(nmb) + ' complex numbers :')

def print_list(listComplex):
    '''
    This function prints the entire list of the complex numbers that are present in listComplex.
    Input : listComplex
    Preconditions : listComplex - is a list
    Output :
    Postconditions :
    '''
    print_number_of_elements(len(listComplex))
    for x in range (0,len(listComplex)):
        print( 'z' + str(x) + ' = ' + toStr(listComplex[x]) )

def help(x):
    '''
    This function prints all the commands that exist in the program, so that the user can use them.
    '''
    print()
    print('The commands for this program are as it follows:')
    print('EXIT, if you want to close the program.')
    print('ADD, if you want to add elements to the sequence.')
    print('PRINT, if you want to print the elements of the sequence.')
    print('SEQUENCE_REAL, if you want to print the list that contains the longest sequence of real numbers from the primary list.')
    print('SEQUENCE_MODULUS, if you want to print the list that contains the longest sequence of complex number with the modulus € [0,10].')

def command_introduction():
    '''
    This function prints the text that is shown to the user before introducing a command.
    '''
    print()
    print('What would you like to do ?')
    print('If you do not know the commands type HELP.')
    print()

def delete_spaces(array):
    '''
    This function delets all the spaces from the string sir.
    Input : sir - a string
    Preconditions :
    Output : res - the string sir but without the spaces
    Postconditions : 
    '''
    array = array + ' '
    previous = -1
    res = ''
    for x in range(0,len(array)):
        if( array[x] == ' ' ):
            aux = array[previous+1:x]
            previous = x
            res = res + aux
    return res

def process_com(command):
    '''
    This function returns the command such that it is correct and interpretable by the program.
    Input : command, a string
    Preconditions :
    Output : command, the string but without spaces and containing only uppercase letters.
    '''
    command = delete_spaces(command)
    command = command.upper()
    return command

def exit():
    '''
    This function writes the text before the ending of the program.
    '''
    print('The program will close now. Bye !')
    print('T. Andreas made it.')

def sign_position( array ):
    '''
    This function return the position where + or - is situated in the array.
    Input : array
    Preconditions : array - string
    Output : x
    Postconditions : x is a natural number, x € [1,len(array)-2]
    '''
    sign_position = -1
    for x in range (1,len(array)):
        if array[x] == '+' or array[x] == '-' :
            return x

def determine_real_part(array):
    '''
    This function returns the real part of a complex number stored in the array string.
    Input : array
    Preconditions : array - a string
    Output : result
    Postconditions : result is a float memorising the real part of the complex number stored in array.
    '''
    auxiliary_array = array[0:sign_position(array)]
    result = float(auxiliary_array)
    return result

def determine_imag_part(array):
    '''
    This function returns the imaginary part of a complex number stored in the array string.
    Input : array
    Preconditions : array - a string
    Output : result
    Postconditions : result is a float memorising the imaginary part of the complex number stored in array.
    '''
    auxiliary_array = array[sign_position(array):(len(array)-1)]
    result = float(auxiliary_array)
    return result
    

def determine_number(array):
    '''
    This function determines the complex number which is stored in array as a string.
    Input : array
    Preconditions : array is a string
    Output : number
    Postconditions : number is a complex number
    '''
    real_part = determine_real_part(array)
    imag_part = determine_imag_part(array)
    number = create_complex_number(real_part, imag_part )
    return number

def add_element():
    '''
    This function returns a complex number read from the keyboard as a string.
    Input :
    Preconditions :
    Output : array
    Postconditions : a complex number as a string
    '''
    array = input()
    array = delete_spaces(array)
    return array

def add_element_ui(listComplex):
    '''
    This function adds a complex number to the list listComplex.
    Input : listComplex
    Preconditions : listComplex is a list of complex numbers
    Output : listComplex
    Postconditions : listComplex contains one more complex number
    '''
    print("Enter the complex number that you want to add, as a + bi with a, b € R :")
    new_number = determine_number(add_element())
    listComplex = add_number_to_list(listComplex, new_number)
    return listComplex


def add_elements(listComplex, nmb):
    '''
    This function adds elements to the list listComplex.
    Input : listComplex, nmb
    Preconditions : listComplex is a list memorising complex numbers
                    nmb is a number representing how many new numbers will be added to listComplex
    Output : listComplex
    Postconditions : listComplex but with nmb more complex numbers in it
    '''
    for x in range (0,nmb) :
        listComplex = add_element_ui(listComplex)
    return listComplex

def add_elements_ui(listComplex):
    '''
    This function reads from the keyboard how many numbers would the user like to add to the list and then adds them.
    Input : listComplex
    Preconditions : listComplex is a list memorising complex numbers
    Output :
    Postconditions :
    '''
    try:
        number = int(input("Enter how many numbers would you like to add : "))
    except ValueError as ve :
        print("Please enter a natural number !")
    add_elements(listComplex,number)
    print("Addition successfully done !")

def check_real(c):
    '''
    This function checks whether a complex number has the imaginary part equal with 0.
    Input : c
    Preconditions : c is a complex number
    Output : True or False
    Postconditions : True if the imaginary part of c is equal with 0
                     False if the imaginary part of c is not equal with 0
    '''
    if c["im"] == 0 :
        return True
    return False

def get_sequence(listComplex, starting_position, final_position):
    '''
    This function goes through listComplex from strating_position to final_position copying the elements in another list.
    Input : listComplex, starting_position, final_position
    Preconditions : listComplex is a list of complex numbers
                    starting_position is a natural number
                    final_position is a natural number
    Output : listReal
    Postconditions : listReal a list containing complex numbers from listComplex
    '''
    list = []
    for x in range (starting_position, final_position + 1):
        list.append(listComplex[x])
    return list

def sequence_real(listComplex):
    '''
    This function determines the starting and ending indexes of the longest sequence that contains complex numbers with the imaginary part equal with 0.
    Input : listComplex
    Preconditions : listComplex is a list containing complex numbers
    Output :
    Postconditions :
    '''
    first_position = 0
    current_lenght = 0
    longest_sequence_lenght = -1
    first_position_longest = -1
    last_position_longest = -1
    for x in range (0,len(listComplex)):
        if check_real(listComplex[x]) == True:
            if current_lenght == 0:
                first_position = x
            current_lenght = current_lenght + 1
            if current_lenght > longest_sequence_lenght:
                longest_sequence_lenght = current_lenght
                first_position_longest = first_position
                last_position_longest = x
        else:
            current_lenght = 0
            first_position = 0
    list = get_sequence(listComplex, first_position_longest, last_position_longest )
    print_list(list)

def check_modulus(c):
    '''
    This function checks whether the modulus of c € [0,10].
    Input : c
    Preconditions : c is a complex number
    Output : True or False
    Postconditions : True if the modulus of c € [0,10]
                     False if the modulus of c < 0 or > 10
    '''
    if math.sqrt(c["re"] * c["re"] + c["im"] * c["im"]) >= 0 and math.sqrt(c["re"] * c["re"] + c["im"] * c["im"]) <= 10 :
           return True
    return False

def sequence_modulus(listComplex):
    '''
    This function determines the starting and ending indexes of the longest sequence that contains complex numbers with the modulus € [0,10].
    Input : listComplex
    Preconditions : listComplex is a list containing complex numbers
    Output :
    Postconditions :
    '''
    first_position = 0
    current_lenght = 0
    longest_sequence_lenght = -1
    first_position_longest = -1
    last_position_longest = -1
    for x in range (0,len(listComplex)):
        if check_modulus(listComplex[x]) == True:
            if current_lenght == 0:
                first_position = x
            current_lenght = current_lenght + 1
            if current_lenght > longest_sequence_lenght:
                longest_sequence_lenght = current_lenght
                first_position_longest = first_position
                last_position_longest = x
        else:
            current_lenght = 0
            first_position = 0
    list = get_sequence(listComplex, first_position_longest, last_position_longest )
    print_list(list)
    
    
# -------------------- TEST FUNCTIONS STARTING --------------------

def test_getters():
    '''
    This function tests whether the get functions work properly.
    '''
    real = 23.45
    imag = 11.23
    c = create_complex_number(real,imag)
    assert get_Real(c) == 23.45
    assert get_Imag(c) == 11.23
    
def test_setters():
    '''
    This function test whether the set functions worl properly.
    '''
    real = 23.45
    imag = 11.23
    c = create_complex_number(real,imag)
    c = set_Real(c,3.33)
    assert c["re"] == 3.33
    c = set_Imag(c,6.9)
    assert c["im"] == 6.9

def test_toStr():
    '''
    This function check whether toStr function return the right string for a complex number.
    '''
    a = create_complex_number(3.21,-4.91)
    assert toStr(a) == '3.21 - 4.91i'
    a = create_complex_number(1.75,2.88)
    assert toStr(a) == '1.75 + 2.88i'

def test_create_complex_number():
    '''
    This function check whether create_complex_number returns the right value.
    '''
    real = 23.45
    imag = 11.23
    c = create_complex_number(real,imag)
    assert get_Real(c) == real
    assert get_Imag(c) == imag

def test_add_number_to_list():
    '''
    This function chekcs whether add_number_to_list returnss the correct list.
    '''
    a = create_complex_number(2.42,-0.8)
    b = create_complex_number(1,2)
    testList = [a]
    testList = add_number_to_list(testList,b)
    assert testList == [a,b]

def test_initialize_list():
    '''
    This function checks whether initialize_list returns the proper list.
    '''
    testList = []
    testList = initialize_list(testList)
    assert testList[2]["re"] == -0.21
    assert testList[9]["im"] == -4.90
    assert testList[9]["re"] == 0
    assert testList[3]["im"] == 0
    assert testList[8]["re"] == 3.21
    assert testList[6]["im"] == 1

def test_delete_spaces():
    '''
    This function checks whether the fhe function delete_spaces delets all the spaces or not.
    '''
    assert delete_spaces('vin si eu la folbal   ') == 'vinsieulafolbal'
    assert delete_spaces('   ana are mere   dar nu   are PERE ') == 'anaaremeredarnuarePERE'

def test_sign_position():
    '''
    This function checks whether the function sign_position return the proper number.
    '''
    test_array = "-0.23-1i"
    assert sign_position(test_array) == 5
    test_array = "1+2.31i"
    assert sign_position(test_array) == 1

def test_determine_real_part():
    '''
    This function checks whether determine_real_part returns the right value ( the real part ).
    '''
    assert determine_real_part("-0.23-1i") == -0.23
    assert determine_real_part("1+2.31i") == 1

def test_determine_imag_part():
    '''
    This function checks whether determine_imag_part returns the right value ( the imag part ).
    '''
    assert determine_imag_part("-0.23-1i") == -1
    assert determine_imag_part("1+2.31i") == 2.31

def test_determine_number():
    '''
    This function checks whether determine_number returns a complex number memorising the real and the imaginary part corretly.
    '''
    test_number = determine_number("-0.23-1i")
    assert test_number["re"] == -0.23
    assert test_number["im"] == -1

def test_check_real():
    '''
    This function tests whether check_real properly determines whether a complex number has the imaginary part equal with 0.
    '''
    test_number = { "re" : -2.123, "im" : 0 }
    assert check_real(test_number) == True
    test_number = { "re" : -2.123, "im" : -2.123 }
    assert check_real(test_number) == False

def test_check_modulus():
    test_number = { "re" : -2.123, "im" : 0 }
    assert check_modulus(test_number) == True
    test_number = { "re" : 6.123, "im" : 123 }
    assert check_modulus(test_number) == False
    
def run_tests():
    '''
    This function runs all the test functions.
    '''
    test_getters()
    test_setters()
    test_toStr()
    test_create_complex_number()
    test_add_number_to_list()
    test_initialize_list()
    test_delete_spaces()
    test_sign_position()
    test_determine_real_part()
    test_determine_imag_part()
    test_determine_number()
    test_check_real()
    test_check_modulus()

# -------------------- TEST FUNCTIONS ENDING --------------------

def main():
    listComplex = []
    listComplex = initialize_list(listComplex)
    print('WELCOME TO THE CANDY SHOP ! This program works with a sequence of complex numbers.')
    print_list(listComplex)
    commands = { "PRINT" : print_list, "HELP" : help, "ADD" : add_elements_ui, "SEQUENCE_REAL" : sequence_real, "SEQUENCE_MODULUS" : sequence_modulus }
    while True:
        command_introduction()
        com = input('Enter command >> ')
        com = process_com(com)
        if com in commands:
            commands[com](listComplex)
        elif( com == 'EXIT' ):
            exit()
            return
        else :
            print('Illegal command. Please try again !')
        
run_tests()
main()
