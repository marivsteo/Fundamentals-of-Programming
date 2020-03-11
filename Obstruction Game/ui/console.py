'''
This is the primary UI module
'''
import sys
from validation.validator import ValidError
import time

class console(object):
    '''
    The console will be interacting with the user through a series of commands.
    '''
    def __ui_exit(self,params):
        if len(params) != 0:
            print("Invalid number of parameters !")
        else:
            print("The game will close ! Bye.")
            sys.exit()
    
    def __ui_initialize(self,params):
        if len(params) == 0:
            print("Invalid number of parameters !")
        else:
            board_size = int(params[0].strip())
            self.__initialized = True
            self.__serv.initialize(board_size)
            self.__ui_print("")
            print("Now the game will begin. You and the AI will take alternative turns.\n")
    
    def __ui_print(self,params):
        if len(params) != 0:
            print("Invalid number of parameters !")
        else:
            board = self.__serv.get_board()
            print(board)
    
    def __ui_place_player(self,params):
        if len(params) != 2:
            print("Invalid number of parameters !")
        else:
            x = int(params[0].strip())
            y = int(params[1].strip())
            self.__serv.place_player(x,y,self.__turns)
            self.__turns = 1
    
    def __ui_place_ai(self):
        self.__serv.place_ai(self.__turns)
        self.__turns = 8
    
    def __ui_going(self):
        return self.__serv.going()
    
    def __init__(self, serv):
        self.__serv = serv
        self.__initialized = False
        self.__turns = 8
        self.__commands = {
            "exit"      : self.__ui_exit,
            "init"      : self.__ui_initialize,
            "print"     : self.__ui_print,
            }
        self.__play = {
            "place"     : self.__ui_place_player
            }
    
    def run(self):
        while True:
            if self.__initialized == False :
                print("In order to initialize the board, use the command <<init>> along with a number !\n")
                raw_command = input("Enter command >> ")
                raw_command.strip()
                command = raw_command.split(' ')
                if command[0] in self.__commands:
                    try:
                        self.__commands[command[0]](command[1:])
                    except ValueError :
                        print("Invalid numerical value !")
                    except ValidError as ValidationError:
                        print(ValidationError)
                else:
                    print("Invalid command. Please enter again !")
            else:
                while self.__ui_going() == True:
                    if self.__turns == 8 :
                        print("It's your turn. In order state your choice, use the command <<place>> along with the 2 coordonates separated by spaces !")
                        raw_command = input("Enter hit >> ")
                        raw_command.strip()
                        command = raw_command.split(' ')
                        if command[0] in self.__play:
                            try:
                                self.__play[command[0]](command[1:])
                            except ValidError as ValidationError:
                                print(ValidationError)  
                            except ValueError as ValueError:
                                print(ValueError)
                        else:
                            print("Please type <<place>> then the coordonates !")
                    else:
                        print("Now it's computer's turn.")
                        time.sleep(1)
                        self.__ui_place_ai()
                if self.__turns == 1:
                    print("Congratiulations, you have beaten the AI !")
                else :
                    print("Unfortunately the AI has beaten you !")
                self.__ui_exit("")