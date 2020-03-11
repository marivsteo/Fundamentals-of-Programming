from Validation.Validators import validDiscipline, validGrade, validStudent
from Bussiness.Controllers import servGrade, servStudent, servDiscipline, UndoService
from Persistance.Repositories import repoGrade, repoStudent, repoDiscipline, Undo_Repository
from Persistance.FileRepo import repoStudentFile
from UI.Console import Console
from analyse.file import mode

import random
from random import randint
from test.sortperf import randfloats
from _stat import filemode

f = mode()
type = f.read_file()

if type[0] == "memory" :
    repoDiscipline = repoDiscipline()
    repoStudent = repoStudent()
    repoGrade = repoGrade()
else:
    repoStudent = repoStudentFile(type[1])
    repoDiscipline = repoDiscipline()
    repoGrade = repoGrade()
    # repoDiscipline = repoDisciplineFile()
    # repoGrade = repoGradeFile()
    
'''

repoDiscipline = repoDiscipline()
repoStudent = repoStudent()
repoGrade = repoGrade()

'''
repoUndo = Undo_Repository()

validDiscipline = validDiscipline()
servDiscipline = servDiscipline(validDiscipline, repoDiscipline)

validGrade = validGrade()
servGrade = servGrade(validGrade,repoGrade)

validStudent = validStudent()
servStudent = servStudent(validStudent, repoStudent,repoUndo)

if type[0] == "memory" :
    disciplineIndex = 0
    disciplinesArray = ["Mate","Romana","Fizica","Sport","Ed. Anteprenoriala", "Chimie","Informatica","TIC","Religie","Engleza","Franceza","Germana","Desen","Muzica"]
    for x in disciplinesArray:
        disciplineIndex = disciplineIndex + 1
        servDiscipline.add_discipline(disciplineIndex,x)
    
    for x in range(1,101):
        servGrade.add_grade(x,randint(1,14),randint(1,100),round(random.uniform(1,10),2))
    
    studentIndex = 0
    studentArray1 = ["Mihai","Ionut","Crbl","Smiley","Ion","Flaviu","Catalin","Gabriel","Cristi","Andrei","Alex","Alexandru","Razvan","Richard"]
    studentArray2 = ["Pop","Popescu","Popa","Denes","Carlos","Stanescu","Eminescu"]
    for x in range(1,101):
        servStudent.add_student(x,random.choice(studentArray1)+random.choice(studentArray2))

servUndo = UndoService(repoUndo,repoStudent,repoDiscipline,repoGrade)

console = Console(servStudent, servDiscipline, servGrade,servUndo)
console.Run()