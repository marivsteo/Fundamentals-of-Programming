from domain.entity import student
from errors.errors import RepoError

class repository(object):
    
    def __init__(self,filename):
        self.__elems = []
        self.__file = filename
        self.readFile()
        
    def readFile(self):
        try:
            with open(self.__file,"r") as file:
                lines = file.readlines()
                for line in lines:
                    if line != "":
                        words = line.strip().split(" ")
                        id = int(words[0].strip())
                        name = words[1].strip() + " " + words[2].strip()
                        attendance = int(words[3].strip())
                        grade = float(words[4].strip())
                        newStudent = student(id,name,attendance,grade)
                        self.add(newStudent)
        except FileNotFoundError:
            print("Inexisting input file !")
        
    def writeFile(self):
        try:
            with open(self.__file,"w") as file:
                for student in self.__elems:
                    file.write(str(student)+"\n")
        except FileNotFoundError:   
            print("Inexisting input file !") 
    
    def add(self,newStudent):
        if newStudent in self.__elems:
            raise RepoError("Repository error !")
            return
        self.__elems.append(newStudent)
        self.writeFile()
    
    def getAll(self):
        return self.__elems[:]
    
    def bonus(self,min,bon):
        for student in self.__elems:
            if student.get_attendance() >= min:
                if student.get_grade()+bon <= 10:
                    student.set_grade(round(student.get_grade()+bon,2))
                else:
                    student.set_grade(10)
        self.writeFile()
        
    def search(self,keyword):
        auxList = []
        for student in self.__elems:
            if student.get_name().find(keyword) != -1:
                auxList.append(student)
        return auxList