"""
test for calculator
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """
    testing calc module
    """
    def test_calc_add(self):
        res=calc.add(5,6)
        self.assertEqual(res,11)

    def test_calc_subtract(self):
        res=calc.subtract(10,15)
        self.assertEqual(res,5)