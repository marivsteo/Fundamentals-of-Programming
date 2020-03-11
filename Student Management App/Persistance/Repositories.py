class RepoError(Exception):
    pass

class repoGrade(object):
    
    def __init__(self):
        self.__grades = []

    def storeGrade(self,newGrade):
        if newGrade in self.__grades:
            raise RepoError("Grades already exists !")
        self.__grades.append(newGrade)
        
    def getAll(self):
        return self.__grades[:]
    
    def searchById(self,id):
        for grade in self.__grades:
            if grade.get_id() == id:
                return grade
        raise RepoError("Inexisting grade !\n")
    
    def updateGrade(self, id,newStudId,newDiscId,newGrade):
        for grad in self.__grades:
            if grad.get_id() == id:
                grad.set_discipline_id(newDiscId)
                grad.set_student_id(newStudId)
                grad.set_value(newGrade)
                return
        raise RepoError("Inexisting grade !\n")
    
    
    def removeGrade(self,id):
        for grad in self.__grades:
            if grad.get_id() == id:
                self.__grades.remove(grad)
                return
        raise RepoError("Inexisting grade !\n")
    
    def existsStudId(self,studId):
        for grad in self.__grades:
            if grad.get_discipline_id() == studId:
                return True
        return False
    
    def removeGradesStud(self,studId):
        while self.existsStudId == True:
            for grad in self.__grades:
                if grad.get_student_id() == studId:
                    self.__grades.remove(grad)
    
    def existsDiscId(self,discId):
        for grad in self.__grades:
            if grad.get_discipline_id() == discId:
                return True
        return False
    
    def removeGradesDisc(self,discId):
        while self.existsDiscId(discId) == True:
            for grad in self.__grades:
                if grad.get_discipline_id() == discId:
                    self.__grades.remove(grad)
    
    def disciplineAverages(self):
        list = []
        for grad in self.__grades:
            discId = grad.get_discipline_id()
            exists = 0
            for el in list:
                if el[0] == discId:
                    exists = 1
            if exists == 0:
                list.append([discId,0,0])
        for grad in self.__grades:
            discId = grad.get_discipline_id
            discGrade = grad.get_value
            for el in list:
                if el[0] == discId:
                    print("asd")
                    list[el[1]] = el[1] + 1
                    list[el[2]] += discGrade
        return list
    
    def studentsFailing(self):
        list = []
        for grad in self.__grades:
            if grad.get_value() < 5:
                if grad.get_student_id not in list:
                    list.append(grad.get_student_id())
        return list
            
class repoDiscipline(object):
    
    def __init__(self):
        self.__disciplines = []
        
    def storeDiscipline(self,newDiscipline):
        if newDiscipline in self.__disciplines:
            raise RepoError("Discipline already exists !")
        self.__disciplines.append(newDiscipline)
    
    def getAll(self):
        return self.__disciplines[:]
    
    def searchById(self,id):
        for discipline in self.__disciplines:
            if discipline.get_id() == id:
                return discipline
        raise RepoError("Inexisting discipline !\n")
    
    def updateDiscipline(self,id,newName):
        for disc in self.__disciplines:
            if disc.get_id() == id:
                disc.set_name(newName)
                return
        raise RepoError("Inexisting discipline !\n")
    
    def removeDiscipline(self,id):
        for disc in self.__disciplines:
            if disc.get_id() == id:
                self.__disciplines.remove(disc)
                return
        raise RepoError("Inexisting discipline !\n")
    
    def searchString(self,string):
        aux = []
        for disc in self.__disciplines:
            if disc.get_name().find(string) != -1:
                aux.append(disc.get_name())
        return aux               

class repoStudent(object):
    
    def __init__(self):
        self.__students = []
        
    def storeStudent(self,newStudent):
        if newStudent in self.__students:
            raise RepoError("Student already exists !")
        self.__students.append(newStudent)
        
    def getAll(self):
        return self.__students[:]
    
    def searchById(self,id):
        for stud in self.__students:
            if stud.get_id() == id:
                return stud
        raise RepoError("Inexisting student !\n")
    
    def updateStudent(self,id,newName):
        for stud in self.__students:
            if stud.get_id() == id:
                stud.set_name(newName)
                return
        raise RepoError("Inexisting student !\n")
    
    def removeStudent(self,id):
        for stud in self.__students:
            if stud.get_id() == id:
                self.__students.remove(stud)
                return
        raise RepoError("Inexisting discipline !\n")
    
    def convertList(self,List):
        aux = []
        for x in List:
            for stud in self.__students :
                if stud.get_id() == x:
                    aux.append(stud.get_name())
        return aux
    
    def searchString(self,string):
        aux = []
        for stud in self.__students:
            if stud.get_name().find(string) != -1:
                aux.append(stud.get_name())
        return aux
        
        
class Undo_Repository(object):
    
    def __init__(self):
        self.__operations = []
        self.__index = 0
        
    def set_index(self, value):
        self.__index = value 
    
    def get_index(self):
        return self.__index
    
    def getAll(self):
        return self.__operations
    
    def add(self, operation, position):
        if position < len(self.__operations):
            self.__operations[position]  = operation 
        else: 
            self.__operations.append(operation)