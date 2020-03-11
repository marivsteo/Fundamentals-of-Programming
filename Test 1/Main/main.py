'''
Created on Dec 18, 2018
@author: Marius
'''
from persistance.repository import repository
from tests.test import test
from validators.validators import validator
from bussines.service import service
from UI.console import console

valid = validator()
repo = repository("Students.txt")
servStudent = service(valid,repo)

c = console(servStudent)
t = test()

#t.run()
c.run()