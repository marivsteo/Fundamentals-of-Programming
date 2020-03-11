'''
Created on 28 Nov 2018

@author: Marius
'''
class Client:
    def __init__(self, clientId, name):
        self._clientId = clientId
        self._name = name

    
    def get_client_id(self):
        return self._clientId


    def get_client_name(self):
        return self._name

    def set_client_name(self, value):
        self._name = value

    def __eq__(self, value):
        if isinstance(value, Client) == False:
            return False
        return self.get_client_id() == value.get_client_id()

    def __str__(self):
        return str(self.get_client_id()) + " " + str(self.get_client_name())
    
    def __repr__(self):
        return str(self)