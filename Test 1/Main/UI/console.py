from validators.validators import ValidError
from persistance.repository import RepoError

class console(object):
       
    def __init__(self, servStudent):
        self.__service = servStudent
        self.__commands = {
            "add"   : self.__ui_add,
            "print" : self.__ui_print,
            "bonus" : self.__ui_bonus,
            "search": self.__ui_search
            }
    
    def run(self):
        while True:
            raw_command = input("Enter command >> ")
            raw_command = raw_command.strip()
            params = raw_command.split(' ')
            if params[0] == "exit":
                print("The program will exit !")
                return
            elif params[0] in self.__commands:
                try:
                    self.__commands[params[0]](params[1:])
                except ValueError :
                    print('Invalid numerical value !')
                except ValidError as validationError :
                    print(validationError)
                except RepoError as repositoryError :
                    print(repositoryError)
            else:
                print("Illegal command !")
    
    def __ui_add(self,params):
        id = int(params[0].strip())
        surname = params[1].strip()
        firstname = params[2].strip()
        name = surname + ' ' + firstname
        attendance = int(params[3].strip())
        grade = float(params[4].strip())
        self.__service.addStudent(id,name,attendance,grade)

    def __ui_print(self,params):
        list = self.__service.getStudents()
        if len(list) < 1:
            print("Empty list !")
        else:
            for student in list:
                print(student)
            
    def __ui_bonus(self,params):
        min = int(params[0].strip())
        bonus = float(params[1].strip())
        self.__service.giveBonus(min,bonus)
        
    def __ui_search(self,params):
        keyword = params[0].strip()
        list = self.__service.searchStudents(keyword)
        list.sort(key = lambda x:x.get_name())
        for student in list:
            print(student)