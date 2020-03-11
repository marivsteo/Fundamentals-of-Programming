from domain.entitity import player

class cons(object):
    '''
    This is the console module.
    '''
    def __init__(self, service):
        self.__service = service
        self.__commands = {
            "print"   : self.ui_print,
            "medals"  : self.ui_medals,
            "stars"   : self.ui_stars
            }
        
    def ui_stars(self,params):
        self.__service.writeStars()    
    
    def ui_print(self,params):
        list = self.__service.getPlayers() 
        for el in list:
            print(str(el) + "," + str(el.get_distance()))
    
    def ui_medals(self,params):
        list = self.__service.getPlayers()
        list.sort( key = player.get_distance, reverse = True )
        place = 1
        for el in list:
            if place == 3 :
                print("Bronze medal goes to :")
                print(el.get_name() + "," + str(el.get_distance()))
                place += 1
            if place == 2 :
                print("Silver medal goes to :")
                print(el.get_name() + "," + str(el.get_distance()))
                place += 1
            if place == 1 :
                print("Gold medal goes to :")
                print(el.get_name() + "," + str(el.get_distance()))
                place += 1
    
    def run(self):
        while True:
            raw_cmd = input("Enter command >> ")
            raw_cmd.strip()
            cmd = raw_cmd.split(" ")
            if cmd[0] == "exit":
                print("The program will be terminated ! Bye.")
                return
            elif cmd[0] == "print":
                self.ui_print(cmd[1:])
            elif cmd[0] == "medals":
                self.ui_medals(cmd[1:])
            elif cmd[0] == "stars" :
                self.ui_stars(cmd[1:])
            else:
                print("Invalid command !\n")