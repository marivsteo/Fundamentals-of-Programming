from Domain.DisciplineEntity import Discipline
from Domain.GradeEntity import Grade
from Domain.StudentEntity import Student
from Domain.UndoAction import Operation, CascadeOperation
from Persistance.Repositories import Undo_Repository, repoStudent, repoDiscipline,repoGrade

class UndoError(Exception):
    pass

class servDiscipline(object):
    
    def __init__(self, validDiscipline, repoDiscipline):
        self.__validDiscipline = validDiscipline
        self.__repoDiscipline = repoDiscipline

    def add_discipline(self,newDisciplineId,newDisciplineName):
        discipline = Discipline(newDisciplineId,newDisciplineName)
        self.__validDiscipline.validate(discipline)
        self.__repoDiscipline.storeDiscipline(discipline)
        
    def get_all_disciplines(self):
        return self.__repoDiscipline.getAll()
    
    def updateDiscipline(self,discId,newName):
        self.__repoDiscipline.updateDiscipline(discId,newName)
        
    def removeDiscipline(self,discId):
        self.__repoDiscipline.removeDiscipline(discId)
        
    def searchDisciplineId(self,id):
        return self.__repoDiscipline.searchById(id)
    
    def searchDisciplineString(self,string):
        return self.__repoDiscipline.searchString(string)

class servGrade(object):
    
    def __init__(self, validGrade, repoGrade):
        self.__validGrade = validGrade
        self.__repoGrade = repoGrade
        
    def add_grade(self,newGradeId,newGradeDiscId,newGradeStudId,newGradeValue):
        grade = Grade(newGradeId,newGradeDiscId,newGradeStudId,newGradeValue)
        self.__validGrade.validate(grade)
        self.__repoGrade.storeGrade(grade)

    def get_all_grades(self):
        return self.__repoGrade.getAll()
    
    def updateGrade(self,gradId,discId,studId,val):
        self.__repoGrade.updateGrade(gradId,discId,studId,val)
        
    def removeGrade(self,gradeId):
        self.__repoGrade.removeGrade(gradeId)
        
    def removeGradesStud(self,studId):
        self.__repoGrade.removeGradesStud(studId)
        
    def removeGradesDisc(self,discId):
        self.__repoGrade.removeGradesDisc(discId)
        
    def getStudentsAtDisc(self,discId):
        students = []
        grades = self.__repoGrade.getAll()
        for grad in grades:
            if grad.get_discipline_id() == discId:
                if grad.get_student_id() not in students:
                    students.append(grad.get_student_id())
        return students
    
    def getStudentsFailing(self):
        return self.__repoGrade.studentsFailing()
    
    def getDisciplinesAverages(self):
        return self.__repoGrade.disciplineAverages()
    
class servStudent(object):
    
    def __init__(self,validStudent,repoStudent,repo_undo):
        self.__validStudent = validStudent
        self.__repoStudent = repoStudent
        self.__repoUndo = repo_undo

    def add_student(self,newStudentId,newStudentName):
        student = Student(newStudentId,newStudentName)
        self.__validStudent.validate(student)
        self.__repoStudent.storeStudent(student)
        ''' Comment undp
        undo = Operation(repoStudent.removeStudent, student, repoStudent.storeStudent, student, "student")
        operation = CascadeOperation()
        operation.add(undo)
        self.__repoUndo.add(operation, self.__repoUndo.get_index())
        self.__repoUndo.set_index(self.__repoUndo.get_index() + 1)
        '''
        
    def get_all_students(self):
        return self.__repoStudent.getAll()
    
    def updateStudent(self,id,newName):
        self.__repoStudent.updateStudent(id,newName)
        
    def removeStudent(self,id):
        self.__repoStudent.removeStudent(id)
        
    def convertList(self,List):
        return self.__repoStudent.convertList(List)
    
    def searchStudentId(self,id):
        return self.__repoStudent.searchById(id)
    
    def searchStudentString(self,string):
        return self.__repoStudent.searchString(string)
    
class UndoService(object):
    
    def __init__(self, undo_repo, repo_students, repo_disciplines, repo_grades):
        self.__repo_students = repo_students
        self.__repo_disciplines = repo_disciplines
        self.__repo_grades = repo_grades
        self.__undo_repo = undo_repo
      
    def get_all(self):
        return self.__undo_repo.getAll()
      
    def perform_undo(self):
        if self.__undo_repo.get_index() > 0:
            list = self.__undo_repo.getAll()
            list = list[self.__undo_repo.get_index() - 1].getAll()
            for operation in list:
                undo_function = operation.get_undo_function()
                elem = operation.get_undo_elem()
                entity = operation.get_entity()
                if entity == "discipline" :
                    undo_function(self.__repo_disciplines, elem)
                elif entity == "student":
                    undo_function(self.__repo_students, elem)
                elif entity == "grade":
                    undo_function(self.__repo_grades, elem)
        
                self.__undo_repo.set_index(self.__undo_repo.get_index() - 1)      
        else:
            raise UndoError("Can't perform any undo! You must perform an action before! ")
    ''' 
    def perform_redo(self):
        if self.__undo_repo.get_index() < len(self.__undo_repo.getAll()):
            list = self.__undo_repo.getAll()
            list = list[self.__undo_repo.get_index() - 1].getAll()
            for operation in list:
                redo_function = operation.get_redo_function()
                elem = operation.get_redo_elem()
                entity = operation.get_entity()
                if entity == "discipline" :
                    redo_function(self.__repo_disciplines, elem)
                elif entity == "student":
                    redo_function(self.__repo_students, elem)
                elif entity == "grade":
                    redo_function(self.__repo_grades, elem)
    
                self.__undo_repo.set_index(self.__undo_repo.get_index() + 1)
        else:
            raise RedoError("Can't perform any redo! You must perform an undo before!")
    '''