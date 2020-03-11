from tests.Test import Test
from business.Service import CookieService
from valid.Validation import CookieValidator
from repo.Repository import Repository
from ui.Console import Console

t=Test()
t.runTests()
repo = Repository()
valid = CookieValidator()
service = CookieService(repo,valid)
console=Console(service)
console.run()