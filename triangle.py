import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_mul(self):
        res = area(10, 12)
        self.assertEqual(res, 60)

    def test_str_mul(self):
        res = area("10", 10)
        self.assertEqual(res, 50)
    
    def test_zero_sum(self):
        res = perimeter(10, 0, 10)
        self.assertEqual(res, 0)
    
    def test_sum(self):
        res = perimeter(2, 4, 6)
        self.assertEqual(res, 12)
    
    def test_str_sum(self):
        res = perimeter(2, "10", 13)
        self.assertEqual(res, 25)

def area(a, h): 
    '''Get length of side and height (a, h) as float, return area (a * h / 2) as float'''
    return a * h / 2 

def perimeter(a, b, c):
    '''Get length of sides (a, b, c) as float, return area (a + b + c) as float''' 
    return a + b + c

