import random

class player(object):
    '''
    This class creates and manages the entity player.
    '''
    def __init__(self,name,dist,speed,wind):
        '''
        The  constructor atributes the properties to the object.
        '''
        self.__name = name
        self.__time = dist
        self.__speed = speed
        self.__wind = wind
        self.__distance = float(self.__time) * (float(self.__speed) + round(random.uniform(-0.5,0.5),2) * int(self.__speed) + int(self.__wind))

    def get_name(self):
        return self.__name

    def get_time(self):
        return self.__time

    def get_speed(self):
        return self.__speed

    def get_wind(self):
        return self.__wind
    
    def get_distance(self):
        return self.__distance
    
    def __str__(self):
        return self.__name + "," + str(self.__time) + "," + str(self.__speed) + "," + str(self.__wind)