'''
Created on Dec 19, 2018
@author: Marius
This is the main module. The console will be started from here.
'''
from bussines.service import serv
from infrastructure.repository import repo
from ui.console import cons
from tests.tests import test

repository = repo("Jumps.txt")
service    = serv(repository)
tst        = test()
console    = cons(service)

tst.runTests()
console.run()