import unittest
from altaml.cat import Cat
from unittest.mock import patch

class TestCat(unittest.TestCase):
    def test_cat_initial_age(self):
        cat = Cat()
        age = cat.getAge()
        
        self.assertIsInstance(age, int)
        self.assertGreaterEqual(age, 5)
        self.assertLessEqual(age, 10)
    
    def test_cat_speaks(self):
        cat = Cat()
        with patch("builtins.print") as mock_print:
            cat.speak()
        mock_print.assert_called_once_with("meow")
        

    
    def test_cat_speaks_more(self):
        cat = Cat()
        with patch("builtins.print") as mock_print:
            cat.speak("AltaML is the best")
        mock_print.assert_called_once_with("AltaML is the best")
            
        

