'''
This is the test module, where all the methods and modules will be tested.
'''
from domain.board import board
from domain.hit import hit
from validation.validator import validator
from errors.error import ValidError
from infrastructure.repository import repository
import unittest

class test(unittest.TestCase):
    '''
    This is the test class, where the modules and methods will be checked one by one.
    '''
    def test_domain_board(self):
        test_board = board(4)
        assert test_board.get_size()   == 4
        assert test_board.get_matrix() == [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]
        test_board.set_size(3)
        assert test_board.get_size()   == 3
        assert test_board.get_matrix() == [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        assert test_board.is_full()    == True
        test_board.place(1,1,8)
        assert test_board.get_matrix() == [['X','X','X'],['X','X','X'],['X','X','X']]
        assert test_board.is_full()    == False
        test_board.place(1,1,1)
        assert test_board.get_matrix() == [['O','O','O'],['O','O','O'],['O','O','O']]
        assert test_board.is_full() == False
        assert test_board.is_inside(-1, 0) == False
        assert test_board.is_inside( 0,-1) == False
        assert test_board.is_inside( 3, 0) == False
        assert test_board.is_inside( 0, 3) == False
        assert test_board.is_inside(-1,-1) == False
        assert test_board.is_inside( 3, 3) == False
        assert test_board.is_inside( 0, 0) == True
        assert test_board.is_inside( 0, 2) == True
        assert test_board.is_inside( 1, 1) == True
        
    def test_domain_hit(self):
        test_hit = hit(1,2,3)
        assert test_hit.get_max() == 3
        assert test_hit.get_x()   == 1
        assert test_hit.get_y()   == 2
        
    def test_validation_validator(self):
        test_validator = validator()
        test_hit = hit(1,2,3)
        assert test_validator.validate_hit(test_hit) == "Valid hit !"
        test_hit = hit(-1,2,3)
        self.assertRaises(ValidError)
        
    def test_infrastructure_repository(self):
        test_repository = repository()
        pass