'''
Created on 28 Nov 2018

@author: Marius
'''
from validation.validators import ValidError
from persistence.repositories import RepoError
from datetime import date
class Console:
    
    def __uiAddClient(self, params):
        if len(params) != 2:
            print("wrong number of params!\n")
            return
        clientId = int(params[0])
        name = params[1]
        self.__servClient.addClient(clientId, name)
        
    def __uiAddBook(self, params):
        if len(params) != 4:
            print("wrong number of params!\n")
            return
        bookId = int(params[0])
        title = params[1]
        author = params[2]
        description = params[3]
        self.__servBook.addBook(bookId, title, author, description)
        
        
    def __uiRentBook(self, params):
        if len(params) != 5:
            print("wrong number of params!\n")
            return
        rentalId = int(params[0])
        start = params[1].date()
        end = params[2].date()
        clientId = int(params[3])
        bookId = int(params[4])
        self.__servRental.addRental(rentalId, start, end, clientId, bookId)
        
    def __uiReturnBook(self, params):
        if len(params) != 1:
            print("worng number of params!\n")
            return
        rentalId = int(params[0])
        self.__servRental.returnBook(rentalId)
        
    def __uiRemoveClient(self, params):
        if len(params) != 1:
            print("wrong number of params!\n")
            return
        clientId = int(params[0])
        self.__servClient.removeClient(clientId-1)
        
    def __uiRemoveBook(self, params):
        if len(params) != 1:
            print("wrong number of params!\n")
            return
        bookId = int(params[0])
        self.__servBook.removeBook(bookId-1)
        
    def __uiPrintClient(self, params):
        if len(params) > 0:
            print("wrong number of params!\n")
            return
        clients = self.__servClient.getAllClients()
        for client in clients:
            print(client)
    
    def __uiPrintBook(self, params):
        if len(params) > 0:
            print("wrong number of params!\n")
            return
        books = self.__servBook.getAllBooks()
        for book in books:
            print(book)
    
    
    def __uiUpdateClient(self, params):
        if len(params) != 2:
            print("wrong number of params!\n")
            return
        clientId = int(params[0])
        name = params[1]
        self.__servClient.updateClient(clientId, name)
    
    
    def __uiUpdateBook(self, params):
        if len(params) != 4:
            print("wrong number of params!\n")
            return
        bookId = int(params[0])
        title = params[1]
        author = params[2]
        description = params[3]
        self.__servBook.updateBook(bookId, title, author, description)
    
    def __uiSearchBookId(self, params):
        if len(params) != 1:
            print("wrong number of params!\n")
            return
        bookId = int(params[0])
        book = self.__servBook.searchBookId(bookId)
        print(book)
    
    def __uiSearchBookTitle(self, params):
        if len(params) != 1:
            print("wrong number of params!\n")
            return
        bookTitle = params[0]
        book = self.__servBook.searchBookTitle(bookTitle)
        print(book)
    
    def __uiSearchBookAuthor(self, params):
        if len(params) != 1:
            print("wrong number of params!\n")
            return
        bookAuthor = params[0]
        book = self.__servBook.searchBookAuthor(bookAuthor)
        print(book)
    
    def __uiSearchClientId(self, params):
        if len(params) != 1:
            print("wrong number of params!\n")
            return
        clientId = int(params[0])
        client = self.__servClient.searchClientId(clientId)
        print(client)
    
    def __uiSearchClientName(self, params):
        if len(params) != 1:
            print("wrong number of params!\n")
            return
        clientName = params[0]
        client = self.__servClient.searchClientName(clientName)
        print(client)
    
    def __uiMostRented(self, params):
        if len(params) > 0:
            print("wrong number of params!\n")
            return
        most = self.__servRental.getMostRented()
        for m in most:
            print(m)
    
    def __uiBestAuthor(self, params):
        if len(params) > 0:
            print("wrong number of params!\n")
            return
        most = self.__servRental.getBestAuthor()
        for m in most:
            print(m)
    
    def __init__(self, servClient, servBook, servRental):
        self.__servClient = servClient
        self.__servBook = servBook
        self.__servRental = servRental
        self.__commands = {
            "addClient" : self.__uiAddClient,
            "addBook" : self.__uiAddBook,
            "removeClient" : self.__uiRemoveClient,
            "removeBook" : self.__uiRemoveBook,
            "printClient" : self.__uiPrintClient,
            "printBook" : self.__uiPrintBook,
            "updateClient" : self.__uiUpdateClient,
            "updateBook" : self.__uiUpdateBook,
            "rentBook" : self.__uiRentBook,
            "returnBook" : self.__uiReturnBook,
            "searchBookId" : self.__uiSearchBookId,
            "searchBookTitle" : self.__uiSearchBookTitle,
            "searchBookAuthor" : self.__uiSearchBookAuthor,
            #"searchBookDescr" : self.__uiSearchBookDescr,
            "searchClientId" : self.__uiSearchClientId,
            "searchClientName" : self.__uiSearchClientName,
            "mostRented" : self.__uiMostRented,
            "bestAuthor" : self.__uiBestAuthor
            }
        
    def run(self):
        while True:
            cmd = input(">>")
            params = cmd.split(" ")
            if cmd == "exit":
                return
            elif params[0] in self.__commands:
                try:
                    self.__commands[params[0]](params[1:])
                except ValueError:
                    print("invalid values!\n")
                except ValidError as ve:
                    print("validation error!\n")
                    print(ve)
                except RepoError as re:
                    print("repository error!\n")
                    print(re)
            else:
                print("invalid command!\n")
        