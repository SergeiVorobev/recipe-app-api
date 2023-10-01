"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module"""
    
    def test_add_numbers(self):
        """Adding two numbers together"""
        res = calc.add(5, 6)
        
        self.assertEqual(res, 11)
        
    def test_substrackt_numbers(self):
        """Test substracting numbers"""
        res = calc.substract(10, 5)
        
        self.assertEqual(res, 5)
        