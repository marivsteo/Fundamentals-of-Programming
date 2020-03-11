import unittest
from Persistance.Repositories import repoStudent
from Domain.StudentEntity import Student

class StudentRepoTest(unittest.TestCase):
 
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test_storeStudent(self):
        repo = repoStudent()
        student1 = (1,"Coco")
        repo.storeStudent(student1)
        assert len(repo.getAll()) == 1
        student2 = (2,"Mojojojo")
        repo.storeStudent(student2)
        assert repo.getAll() == [student1,student2]
        
    def test_getAll(self):
        repo = repoStudent()
        student1 = (1,"Keke")
        student2 = (2,"Mimi")
        repo.storeStudent(student1)
        repo.storeStudent(student2)
        aux = repo.getAll()
        assert aux == [student1,student2]
        
    def test_searchById(self):
        repo = repoStudent()
        student1 = (1,"Keke")
        student2 = (2,"Mimi")
        repo.storeStudent(student1)
        repo.storeStudent(student2)
        rez = repo.searchById(1)
        assert rez == student1
        
    def test_removeStudent(self):
        repo = repoStudent()
        student1 = (1,"Keke")
        student2 = (2,"Mimi")
        repo.storeStudent(student1)
        repo.storeStudent(student2)
        repo.removeStudent(1)
        assert repo.getAll() == [student2]
        
    def test_convertList(self):
        repo = repoStudent()
        student1 = (1,"Keke")
        student2 = (2,"Mimi")
        repo.storeStudent(student1)
        repo.storeStudent(student2)
        auxList = [1]
        repo.convertList(auxList)
        assert auxList["Keke"]
        