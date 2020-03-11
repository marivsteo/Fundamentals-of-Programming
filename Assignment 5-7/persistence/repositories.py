'''
Created on 28 Nov 2018

@author: Marius
'''
from entities.book import Book
from entities.client import Client

class RepoError(Exception):
    pass

class RepoClient:
    
    def __init__(self):
        self.__clients = []
        
    def searchById(self, clientId):
        for client in self.__clients:
            if client.get_client_id() == clientId:
                return client
        raise RepoError("Inexisting client!")
    
    def searchByName(self, clientName):
        for client in self.__clients:
            if client.get_client_name() == clientName:
                return client
        raise RepoError("Inexisting client!")
    
    def storeClient(self, client):
        if client in self.__clients:
            raise RepoError("Existing client!")
        self.__clients.append(client)
        
    def getAll(self):
        return self.__clients[:]
    
    def __len__(self):
        return len(self.__clients)
    
    def __str__(self):
        r = ""
        for e in self._clients:
            r += str(e)
            r += "\n"
        return r
    
    def deleteClient(self, clientId):
        self.__clients.pop(clientId)

class RepoBook:
    
    def __init__(self):
        self.__books = []
        
    def searchById(self, bookId):
        for book in self.__books:
            if book.get_book_id() == bookId:
                return book
        raise RepoError("Inexisting book!")
    
    def searchByTitle(self, bookTitle):
        for book in self.__books:
            if book.get_title() == bookTitle:
                return book
        raise RepoError("Inexisting title!")
    
    def searchByAuthor(self, bookAuthor):
        for book in self.__books:
            if book.get_author() == bookAuthor:
                return book
        raise RepoError("Inexisting author!")
    
    def storeBook(self, book):
        if book in self.__books:
            raise RepoError("Existing book!")
        self.__books.append(book)
        
    def getAll(self):
        return self.__books[:]
    
    def __len__(self):
        return len(self.__books)
    
    def __str__(self):
        r = ""
        for e in self._books:
            r += str(e)
            r += "\n"
        return r
        
    def deleteBook(self, bookId):
        self.__books.pop(bookId)
        
class RepoRental:
    
    def __init__(self):
        self.__rentals = []
        
    def searchById(self, rentalId):
        for rental in self.__rentals:
            if rental == rentalId:
                return rental
        raise RepoError("Inexisting rental!")
    
    def storeRental(self, rental):
        if rental in self.__rentals:
            raise RepoError("Existing rental!")
        self.__rentals.append(rental)
        
    def getAll(self):
        return self.__rentals[:]
    
    def searchByBookId(self, rental):
        for r in self.__rentals:
            if r.get_book().get_book_id() == rental.get_book().get_book_id():
                return r
        return False
    
    def __len__(self):
        return len(self.__rentals)
    
    def __str__(self):
        r = ""
        for e in self._rentals:
            r += str(e)
            r += "\n"
        return r        
