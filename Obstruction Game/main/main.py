from ui.console import console
from bussines.service import service
from infrastructure.repository import repository
from validation.validator import validator

repo  = repository()
valid = validator()
serv  = service(repo,valid)
cons  = console(serv)

cons.run()