from Persistance.Repositories import RepoError
from Validation.Validators import ValidError
from Bussiness.Controllers import UndoService

class Console(object):
    
    def __ui_addStudent(self,params):
        if len(params) != 2:
            print("Invalid number of parameters !")
            return
        newStudentId = int(params[0])
        newStudentName = params[1]
        self.__servStudent.add_student(newStudentId,newStudentName) 
        # student = student(newStudentId,newStudentName)
        #self.__ServUndo.__repoUndo.addAction((self.__servStudent.removeStudent(),()))
        
    def __ui_addGrade(self,params):
        if len(params) != 4:
            print("Invalid number of parameters !")
            return
        newGradeId = int(params[0])
        newGradeDiscId = int(params[1])
        newGradeStudId = int(params[2])
        newGradeValue = float(params[3])
        self.__servGrade.add_grade(newGradeId,newGradeDiscId,newGradeStudId,newGradeValue)
    
    def __ui_addDiscipline(self,params):
        if len(params) != 2:
            print("Invalid number of parameters !")
            return
        newDisciplineId = int(params[0])
        newDisciplineName = params[1]
        self.__servDiscipline.add_discipline(newDisciplineId,newDisciplineName)
    
    def __ui_printStudents(self,params):
        if len(params) != 0:
            print("Invalid number of parameters !")
            return
        students = self.__servStudent.get_all_students()
        print("The students are :")
        for stud in students:
            print(stud)
    
    def __ui_printGrades(self,params):
        if len(params) != 0:
            print("Invalid number of parameters !")
            return
        grades = self.__servGrade.get_all_grades()
        print("The grades are :")
        for grad in grades:
            print(grad)
            
    def __ui_printDisciplines(self,params):
        if len(params) != 0:
            print("Invalid number of parameters !")
            return
        disciplines = self.__servDiscipline.get_all_disciplines()
        print("The disciplines are :")
        for disc in disciplines:
            print(disc)
    
    def __ui_updateStudent(self,params):
        if len(params) != 2:
            print("Invalid number of parameters !")
            return
        studentId = int(params[0])
        newStudentName = params[1]
        self.__servStudent.updateStudent(studentId,newStudentName)
    
    def __ui_updateGrade(self,params):
        if len(params) != 4:
            print("Invalid number of parameters !")
            return
        gradeId = int(params[0])
        disId = int(params[1])
        stuId = int(params[2])
        val = float(params[3])
        self.__servGrade.updateGrade(gradeId,disId,stuId,val)
    
    def __ui_updateDiscipline(self,params):
        if len(params) != 2:
            print("Invalid number of parameters !")
            return
        discId = int(params[0])
        newDiscName = params[1]
        self.__servDiscipline.updateDiscipline(discId,newDiscName)
    
    def __ui_removeStudent(self,params):
        if len(params) != 1:
            print("Invalid number of parameters !")
            return
        studId = int(params[0])
        self.__servStudent.removeStudent(studId)
        self.__servGrade.removeGradesStud(studId)
    
    def __ui_removeGrade(self,params):
        if len(params) != 1:
            print("Invalid number of parameters !")
            return
        gradeId = int(params[0])
        self.__servGrade.removeGrade(gradeId)
    
    def __ui_removeDiscipline(self,params):
        if len(params) != 1:
            print("Invalid number of parameters !")
            return
        discId = int(params[0])
        self.__servDiscipline.removeDiscipline(discId)
        self.__servGrade.removeGradesDisc(discId)
    
    def __ui_printStudentsAtDisc(self,params):
        if len(params) != 1:
            print("Invalid number of parameters !")
            return
        discId = int(params[0])
        list = self.__servGrade.getStudentsAtDisc(discId)
        list = self.__servStudent.convertList(list)
        list.sort()
        print(list)
        
    def __ui_printStudentsFailing(self,params):
        if len(params) != 0:
            print("Invalid number of parameters !")
            return
        list = self.__servGrade.getStudentsFailing()
        list = self.__servStudent.convertList(list)
        list.sort()
        print(list)
    
    def __ui_search(self,params):
        if len(params) != 2:
            print("Invalid number of parameters !")
            return
        if params[0] != "discipline" and params[0] != "student":
            print("Invalid second parameter !")
            return
        try:
            id = int(params[1])
            res = -1
            if params[0] == "student":
                res = self.__servStudent.searchStudentId(id)
            else:
                res = self.__servDiscipline.searchDisciplineId(id)
            print(res)
        except ValueError as ve:
            if params[0] == "student":
                res = self.__servStudent.searchStudentString(params[1])
            else:
                res = self.__servDiscipline.searchDisciplineString(params[1])
            if len(res) >0:
                print(res)
            else:
                print("No match !")
                
    def __ui_undo(self,params):
        self.__ServUndo.perform_undo()
        '''
        aux = self.__ServUndo.get_all()
        print(aux)
        '''
        
    def __init__(self, servStudent, servDiscipline, servGrade,servUndo):
        self.__servStudent = servStudent
        self.__servDiscipline = servDiscipline
        self.__servGrade = servGrade
        self.__ServUndo = servUndo
        self.__commands = {
            "addStudent"        : self.__ui_addStudent,
            "addGrade"          : self.__ui_addGrade,
            "addDiscipline"     : self.__ui_addDiscipline,
            "printStudents"     : self.__ui_printStudents,
            "printGrades"       : self.__ui_printGrades,
            "printDisciplines"  : self.__ui_printDisciplines,
            "updateStudent"     : self.__ui_updateStudent,
            "updateGrade"       : self.__ui_updateGrade,
            "updateDiscipline"  : self.__ui_updateDiscipline,
            "removeStudent"     : self.__ui_removeStudent,
            "removeGrade"       : self.__ui_removeGrade,
            "removeDiscipline"  : self.__ui_removeDiscipline,
            "printStudentsAtDiscipline" : self.__ui_printStudentsAtDisc,
            "printStudentsFailing"      : self.__ui_printStudentsFailing,
            "search"                    : self.__ui_search,
            "undo"                      : self.__ui_undo,
            }
        
    def Run(self):
        while True:
            command = input("Enter command >> ")
            cmd = command.split(' ')
            if cmd[0] == "exit" :
                return
            elif cmd[0] in self.__commands:
                try:
                    self.__commands[cmd[0]](cmd[1:])
                except ValueError as VE:
                    print("Invalid numerical value !")
                except RepoError as re:
                    print("Repository error !")
                    print(re)
                except ValidError as ve:
                    print("Validation error !")
                    print(ve)
            else:
                print("Invalid command !")       