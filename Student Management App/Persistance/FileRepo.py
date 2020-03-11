'''
Created on Dec 11, 2018
@author: andreas
'''
from Persistance.Repositories import repoGrade, repoDiscipline, repoStudent
from Domain.DisciplineEntity import Discipline
from Domain.GradeEntity import Grade
from Domain.StudentEntity import Student
from fileinput import filename

class repoDisciplineFile():
    
    def __init__(self,filename):
        self.__repo =repoDiscipline
        self.__filename = filename.strip()
        self.__readAllFromFile()
        
    def __readAllFromFile(self):
        try:
            with open(self.__filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line != "":
                        words = line.strip().split(",")
                        ident = int(words[0].strip())
                        name = words[1].strip()
                        disc = Discipline(ident,name)
                        self.__repo.storeDiscipline(disc)
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)
            
    def __writeAllToFile(self):
        try:
            with open(self.__filename,"w") as f:
                for elem in self.__repo.getAll():
                    f.write(str(elem)+"\n")
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)

    def storeDiscipline(self,newDiscipline):
        self.__repo.storeDiscipline(newDiscipline)
        self.__writeAllToFile()
    
    def getAll(self):
        self.__repo.getAll()
    
    def searchById(self,id):
        self.__repo.searchById(id)
    
    def updateDiscipline(self,id,newName):
        self.__repo.updateDiscipline(id, newName)
        self.__writeAllToFile()
    
    def removeDiscipline(self,id):
        self.__repo.removeDiscipline(id)
        self.__writeAllToFile()
    
    def searchString(self,string):
        self.__repo.searchString(string)
    
class repoGradeFile():
    
    def __init__(self,filename):
        self.__repo = repoGrade()
        self.__filename = filename.strip()
        self.__readAllFromFile()
        
    def __readAllFromFile(self):
        try:
            with open(self.__filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line != "":
                        words = line.strip().split(",")
                        ident = int(words[0].strip())
                        disc = int(words[1].strip())
                        stud = int(words[2].strip())
                        mark = float(words[3].strip())
                        grade = Grade(ident,disc,stud,mark)
                        self.__repo.storeGrade(grade)
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)
            
    def __writeAllToFile(self):
        try:
            with open(self.__filename,"w") as f:
                for elem in self.__repo.getAll():
                    f.write(str(elem)+"\n")
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)
            
    def storeGrade(self,newGrade):
        self.__repo.storeGrade(newGrade)
        self.__writeAllToFile()
        
    def getAll(self):
        return self.__repo.getAll()
        self.__writeAllToFile()
    
    def searchById(self,id):
        self.__repo.searchById(id)
        self.__writeAllToFile()
    
    def updateGrade(self, id,newStudId,newDiscId,newGrade):
        self.__repo.updateGrade(id, newStudId, newDiscId, newGrade)
        self.__writeAllToFile()
    
    def removeGrade(self,id):
        self.__repo.removeGrade(id)
        self.__writeAllToFile()
    
    def existsStudId(self,studId):
        self.__repo.existsStudId(studId)
    
    def removeGradesStud(self,studId):
        self.__repo.removeGradesStud(studId)
        self.__writeAllToFile()
    
    def existsDiscId(self,discId):
        self.__repo.existsDiscId(discId)
    
    def removeGradesDisc(self,discId):
        self.__repo.removeGradesDisc(discId)
        self.__writeAllToFile()
    
    def disciplineAverages(self):
        self.__repo.disciplineAverages()
    
    def studentsFailing(self):
        self.__repo.studentsFailing()

class repoStudentFile():
    
    def __init__(self,filename):
        self.__repo = repoStudent()
        self.__filename = filename.strip()
        self.__readAllFromFile()
        
    def __readAllFromFile(self):
        try:
            with open(self.__filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line != "":
                        words = line.strip().split(",")
                        ident = int(words[0].strip())
                        name = words[1].strip()
                        student = Student(ident,name)
                        self.__repo.storeStudent(student)
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)
            
    def __writeAllToFile(self):
        try:
            with open(self.__filename,"w") as f:
                for elem in self.__repo.getAll():
                    f.write(str(elem)+"\n")
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)
    
    def storeStudent(self,newStudent):
        self.__repo.storeStudent(newStudent)
        self.__writeAllToFile()
    
    def getAll(self):
        return self.__repo.getAll()
        self.__writeAllToFile()
    
    def searchById(self,id):
        self.__repo.searchById(id)
        self.__writeAllToFile()
    
    def updateStudent(self,id,newName):
        self.__repo.updateStudent(id, newName)
        self.__writeAllToFile()
    
    def removeStudent(self,id):
        self.__repo.removeStudent(id)
        self.__writeAllToFile()
    
    def convertList(self,List):
        self.__repo.convertList(List)
        self.__writeAllToFile()
    
    def searchString(self,string):
        self.__repo.searchString(string)
        self.__writeAllToFile()


