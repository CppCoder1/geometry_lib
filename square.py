import unittest

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_mul(self):
        res = area(12)
        self.assertEqual(res, 144)

    def test_str_mul(self):
        res = area("10")
        self.assertEqual(res, 100)
    
    def test_zero_sum(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_sum(self):
        res = perimeter(4)
        self.assertEqual(res, 16)
    
    def test_str_sum(self):
        res = perimeter("10")
        self.assertEqual(res, 100)

def area(a):
    '''Get length of side (a) as float, return area (a ** 2) as float'''
    return a * a


def perimeter(a):
    '''Get length of side (a) as float, return perimeter (4 * a) as float'''
    return 4 * a