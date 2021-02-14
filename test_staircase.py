from unittest import TestCase
from main import Staircase

class Test_Staircase(TestCase):
    def tests_if_there_is_staircase_class(self):
        if Staircase(4):
            return

    def tests_if_staircase_is_receiving_the_parameter(self):
        result = Staircase(4)
        assert result.n == 4

    def test_if_there_is_a_printing_function(self):
        result = Staircase(4)
        if result.printing():
            return