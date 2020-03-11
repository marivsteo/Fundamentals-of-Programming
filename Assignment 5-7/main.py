'''
Created on 28 Nov 2018

@author: Marius
'''
from validation.validators import validClient,validBook,validRental
from persistence.repositories import RepoBook,RepoClient,RepoRental
from business.controllers import ServBook,ServClient,ServRental
from ui.console import Console

repoBook = RepoBook()
validBook = validBook()
servBook = ServBook(validBook,repoBook)

servBook.addBook(1, "Papillon", "Henri Charriere", "Based on a real story")
servBook.addBook(2, "Mythology", "Thor Sonofodin", "Book about Norse Mythology")



repoClient = RepoClient()
validClient = validClient()
servClient = ServClient(validClient,repoClient)

servClient.addClient(1, "JeanValjean")
servClient.addClient(2, "AlanWatts")



repoRental = RepoRental()
validRental = validRental()
servRental = ServRental(validRental,repoRental,repoClient,repoBook)



c= Console(servClient,servBook,servRental)
c.run()