'''
Created on 28 Nov 2018

@author: Marius
'''
class Book:
    
    def __init__(self, bookId, title, author, description):
        self._bookId = bookId
        self._title = title
        self._author = author
        self._description = description

    def get_book_id(self):
        return self._bookId


    def get_title(self):
        return self._title


    def get_description(self):
        return self._description


    def get_author(self):
        return self._author


    def set_title(self, value):
        self.__title = value


    def set_description(self, value):
        self.__description = value


    def set_author(self, value):
        self.__author = value

    bookId = property(get_book_id, None, None, None)
    title = property(get_title, set_title, None, None)
    description = property(get_description, set_description, None, None)
    author = property(get_author, set_author, None, None)
        
    def __eq__(self, value):
        if isinstance(value, Book) == False:
            return False
        return self._bookId == value._bookId
    
    def __str__(self):
        return str(str(self.get_book_id()) + " " + self.get_title() + " | " + self.get_author() + " | " + self.get_description())