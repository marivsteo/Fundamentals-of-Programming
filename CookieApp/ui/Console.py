from errors.Errors import RepoError, ValidError
class Console(object):
    
    
    def __init__(self, __service):
        self.__service = __service

    def __uiAddCookie(self,params):
        if len(params)!= 3:
            print("invalid no of params!")
            return 
        ident = int(params[0])
        name = params[1]
        weight = float(params[2])
        self.__service.addCookie(ident,name,weight)
    
    def __uiPrintCookies(self,params):
        if len(params)!=0:
            print("invalid no of params!")
            return
        cookies = self.__service.getAllCookies()
        if len(cookies)==0:
            print("Empty list!")
            return
        s = ""
        for x in cookies:
            s+=str(x)+"\n"
        print(s)
        
    def run(self):
        commands={"add":self.__uiAddCookie,"print":self.__uiPrintCookies}
        while True:
            cmd = input(">>")
            params = cmd.split(" ")
            if cmd == "exit":
                return 
            elif params[0] in commands:
                try:
                    commands[params[0]](params[1:])
                except ValueError:
                    print("invalid numeric value given!")
                except RepoError as re:
                    print("Repository Error:")
                    print(re)
                except ValidError as ve:
                    print("Validation Error:")
                    print(ve)    
            else:
                print("invalid command!")