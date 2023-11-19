import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_mul(self):
        res = area(10, 12)
        self.assertEqual(res, 120)

    def test_str_mul(self):
        res = area("10", 10)
        self.assertEqual(res, 100)
    
    def test_zero_sum(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 0)
    
    def test_sum(self):
        res = perimeter(2, 4)
        self.assertEqual(res, 12)
    
    def test_str_sum(self):
        res = perimeter(2, "10")
        self.assertEqual(res, 24)

def area(a : float, b : float) -> float:
    '''Get length of sides (a, b) as float, return area (a*b) as float'''
    return a * b

def perimeter(a : float, b : float) -> float:
    '''Get length of sides (a, b) as float, return perimeter (2 * (a + b)) as float'''
    return (a + b) * 2