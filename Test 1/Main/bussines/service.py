from domain.entity import student

class service(object):
    
    def __init__(self, valid, repo):
        self.__valid = valid
        self.__repo = repo
    
    def addStudent(self,id,name,attendance,grade):
        newStudent = student(id,name,attendance,grade)
        self.__valid.validate(newStudent)
        self.__repo.add(newStudent)

    def getStudents(self):
        return self.__repo.getAll()
    
    def giveBonus(self,min,bon):
        self.__repo.bonus(min,bon)
        
    def searchStudents(self,keyword):
        return self.__repo.search(keyword)
    
    '''
    def sortList(self,list):
        for i in range(len(list)):
            for j in range(i+1,len(list)):
                if list[i].get_name() > list[j].get_name():
                    aux = list[i]
                    list[i] = list[j]
                    list[j] = aux
        return list
    '''