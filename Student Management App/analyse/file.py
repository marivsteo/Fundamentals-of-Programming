'''
Created on Dec 11, 2018

@author: andreas
'''

class mode():
    def __init__(self):
        self.__filename = "settings.properties.txt"
        
    def __get_mode(self,line):
        words = line.split(' ')
        if len(words) == 3:
            return words[2]
        else:
            return
        
    def read_file(self):
        with open(self.__filename,"r") as f:
            line = f.readline()
            type = self.__get_mode(line)
            line = f.readline()
            studentsFile = self.__get_mode(line)
            line = f.readline()
            disciplinesFile = self.__get_mode(line)
            line = f.readline()
            gradesFile = self.__get_mode(line)
            return [type, studentsFile, disciplinesFile, gradesFile]