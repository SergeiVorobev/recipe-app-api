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
        