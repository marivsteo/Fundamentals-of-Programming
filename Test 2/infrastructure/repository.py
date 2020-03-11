from domain.entitity import player

class repo(object):
    '''
    This is the repository class where all the objects will be stored
    '''
    def __init__(self,filename):
        self.__elems  = []
        self.__file   = filename 
        self.__readFile()

    def __readFile(self):
        '''
        This function opens and reads the file, then adds each player in the list elems.
        If the file is not found it will throw an error.
        '''
        try:
            with open(self.__file,"r") as file:
                lines = file.readlines()
                for line in lines:
                    if line != "":
                        params = line.split(",")
                        name   = params[0].strip()
                        dist   = params[1].strip()
                        speed  = params[2].strip()
                        wind   = params[3].strip()
                        newPlayer = player(name,dist,speed,wind)
                        self.__elems.append(newPlayer)
        except FileNotFoundError:
            print("File not found !\n")
            
    def writeStarsInFile(self):
        '''
        This function opens and writes the Stars.txt file.
        In the file there will be * and names, accordingly to the order and the distance of the jumps.
        '''
        try:
            with open("Stars.txt","w") as file:
                for el in self.__elems:
                    dist = el.get_distance()
                    for i in range(0,int(dist)//50):
                        file.write("*")
                    file.write(el.get_name())
        except FileNotFoundError:
            print("File not found !\n")

    def getElements(self):
        '''
        This function returns the list of all players.
        '''
        return self.__elems[:]