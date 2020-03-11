'''
Created on 28 Nov 2018

@author: Marius
'''
from entities.client import Client
from entities.book import Book
from entities.rental import Rental, mostRentedDTO, bestAuthorDTO
import datetime

class ServClient:
    
    def __init__(self, validClient, repoClient):
        self.__validClient = validClient
        self.__repoClient = repoClient
        
    def addClient(self, clientId, name):
        client = Client(clientId, name)
        self.__validClient.validate(client)
        self.__repoClient.storeClient(client)
        
    def removeClient(self, clientId):
        self.__repoClient.deleteClient(clientId)
        
    def updateClient(self, clientId, name):
        client = self.__repoClient.searchById(clientId)
        client.set_client_name(name)
        
    def getAllClients(self):
        return self.__repoClient.getAll()
    
    def searchClientId(self, clientId):
        return self.__repoClient.searchById(clientId)
    
    def searchClientName(self, clientName):
        return self.__repoClient.searchByName(clientName)
    
class ServBook:
    
    def __init__(self, validBook, repoBook):
        self.__validBook = validBook
        self.__repoBook = repoBook
        
    def addBook(self, bookId, title, author, description):
        book = Book(bookId, title, author, description)
        self.__validBook.validate(book)
        self.__repoBook.storeBook(book)
        
    def removeBook(self, bookId):
        self.__repoBook.deleteBook(bookId)
        
    def updateBook(self, bookId, title, author, description):
        book = self.__repoBook.searchById(bookId)
        book.set_title(title)
        book.set_author(author)
        book.set_description(description)
        
    def getAllBooks(self):
        return self.__repoBook.getAll()
    
    def searchBookId(self, bookId):
        return self.__repoBook.searchById(bookId)
    
    def searchBookTitle(self, bookTitle):
        return self.__repoBook.searchByTitle(bookTitle)
    
    def searchBookAuthor(self, bookAuthor):
        return self.__repoBook.searchByAuthor(bookAuthor)
    
class ServRental:
    
    def __init__(self, validRental, repoRental, repoClient, repoBook):
        self.__validRental = validRental
        self.__repoRental = repoRental
        self.__repoClient = repoClient
        self.__repoBook = repoBook
        
    def addRental(self, rentalId, start, end, clientId, bookId, date=None):
        client = self.__repoClient.searchById(clientId)
        book = self.__repoBook.searchById(bookId)
        rental = Rental(rentalId, start, end, date, client, book)
        self.__validRental.validate(rental)
        self.__repoRental.storeRental(rental)
        
    def removeRental(self, rentalId):
        rental = self.__repoRental.searchById(rentalId)
        return self.__repository.delete(rental)
    
    def returnBook(self, rentalId):
        rental = self.__repoRental.searchById(rentalId)
        now = datetime.date.today()
        rental.set_date(now)
        
    def getMostRented(self):
        books = {}
        rentals = self.__repoRental.getAll()
        for rental in rentals:
            bookId = rental.get_book.get_book_id()
            if bookId not in books:
                books[bookId] = [rental.get_book.get_title(),0]
            books[bookId][1] += 1
        rez = []
        for b in books:
            book = books[b]
            rez.append(mostRentedDTO(book[0],book[1]))
        rez.sort(key = lambda x: x.get_times_rented(), reverse = True)
        return rez
    
    def getBestAuthor(self):
        authors = {}
        rentals = self.__repoRental.getAll()
        for rental in rentals:
            author = rental.get_book.get_author()
            if author not in authors:
                authors[author] = [rental.get_book.get_author(),0]
            authors[author][1] += 1
        rez = []
        for a in authors:
            author = authors[a]
            rez.append(bestAuthorDTO(author[0],author[1]))
        rez.sort(key = lambda x: x.get_times_rented(), reverse = True)
        return rez
            