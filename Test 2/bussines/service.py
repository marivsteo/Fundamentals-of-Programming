from domain.entitity import player

class serv(object):
    '''
    This is the service class, in the service module.
    The service is the layer between ui and repository, and handles the players.
    ''' 
    def __init__(self, repository):
        self.__repository = repository
        
    def getPlayers(self):
        '''
        This function returns a list with all the players.
        '''
        return self.__repository.getElements()
    
    def writeStars(self):
        '''
        This function writes stars in a file then followed with the player's name performance.
        1 star = 50 meter.
        '''
        self.__repository.writeStarsInFile()