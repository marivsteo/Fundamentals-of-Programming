'''
Created on Feb 6, 2019
@author: Marius
'''
from ui import Console
from bussines import Service
from persistance import Repository
from validation import Validator

repository = Repository()
validator = Validator()
service = Service(repository,validator)
console = Console(service)
console.run()