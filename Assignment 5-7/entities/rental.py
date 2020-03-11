'''
Created on 28 Nov 2018

@author: Marius
'''
class Rental:
    def __init__(self, rentalId, start, end, date, client, book):
        self._rentalId = rentalId
        self._client = client
        self._book = book
        self._start = start
        self._end = end
        self.__date = date

    def get_rental_id(self):
        return self.__rentalId


    def get_client(self):
        return self.__client


    def get_book(self):
        return self.__book


    def get_start(self):
        return self.__start


    def get_end(self):
        return self.__end


    def get_date(self):
        return self.__date


    def set_client(self, value):
        self.__client = value


    def set_book(self, value):
        self.__book = value


    def set_start(self, value):
        self.__start = value


    def set_end(self, value):
        self.__end = value


    def set_date(self, value):
        self.__date = value

    
    def __len__(self):
        return (self._end - self._start).days + 1

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Rental: " + str(self.get_rental_id()) + "\nBook: " + str(self.get_book()) + "\nClient: " + str(self.get_client()) + "\nPeriod: " + self.get_start().strftime("%Y-%m-%d") + " to " + self.get_end().strftime("%Y-%m-%d")
    
    rentalId = property(get_rental_id, None, None, None)
    client = property(get_client, set_client, None, None)
    book = property(get_book, set_book, None, None)
    start = property(get_start, set_start, None, None)
    end = property(get_end, set_end, None, None)
    date = property(get_date, set_date, None, None)
    
class mostRentedDTO(object):
    
    def __init__(self, title, timesRented):
        self.__title = title
        self.__timesRented = timesRented
        
    def get_times_rented(self):
        return self.__timesRented

    def __str__(self):
        return self.__title + " was rented " + str(self.__timesRented) + " times."
    
    timesRented = property(get_times_rented, None, None, None)
    
class bestAuthorDTO(object):
    
    def __init__(self, author, timesRented):
        self.__author = author
        self.__timesRented = timesRented
        
    def get_times_rented(self):
        return self.__timesRented

    def __str__(self):
        return self.__author + " was rented " + str(self.__timesRented) + " times."
    
    timesRented = property(get_times_rented, None, None, None)