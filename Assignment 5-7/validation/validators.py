'''
Created on 28 Nov 2018

@author: Marius
'''

from entities.client import Client
from entities.book import Book
from entities.rental import Rental
import datetime
from persistence.repositories import RepoRental

class ValidError(Exception):
    pass

class validClient:
    
    def __init__(self):
        pass
    
    def validate(self, client):
        errors = ""
        if isinstance(client, Client) == False:
            errors += "this is not even a client!\n"
        if client.get_client_id()<0:
            errors += "invalid id!\n"
        if len(client.get_client_name()) == 0:
            errors += "invalid name!\n"
        if len(errors)>0:
            raise ValidError(errors)
        
class validBook:
    
    def __init__(self):
        pass
    
    def validate(self, book):
        errors = ""
        if isinstance(book, Book) == False:
            errors += "this is not even a book!\n"
        if book.get_book_id()<0:
            errors += "invalid id!\n"
        if len(book.get_title()) == 0:
            errors += "invalid title!\n"
        if len(book.get_author()) == 0:
            errors += "invalid author!\n"
        if len(book.get_description()) == "":
            errors += "invalid description!\n"
        if len(errors)>0:
            raise ValidError(errors)
        
class validRental:
    
    def __init__(self):
        pass
    
    def validate(self, rental):
        errors = ""
        if isinstance(rental, Rental) == False:
            errors += "this is not even a rental!\n"
        now = datetime.date.today()
        if rental.get_start().date() < now:
            errors += "rental starts before now!\n"
        if rental.searchByBookId() != False:
            if rental.get_start.date() < rental.searchByBookId().get_end.date():
                errors += "book is already rented to someone else\n"
        if rental.get_rental_id()<0:
            errors += "invalid id!\n"
        if rental.get_start().date() > rental.get_end().date():
            errors += "due date has to be after start date\n"
        if len(rental) < 1:
            errors += "rent is for at least 1 day\n"
        if len(errors) > 0:
            raise ValidError(errors)
        