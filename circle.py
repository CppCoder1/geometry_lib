import math
import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_mul(self):
        res = area(10)
        self.assertEqual(res, 100 * math.pi)
    
    def test_str_mul(self):
        res = area("10")
        self.assertEqual(res, 100 * math.pi)
    
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 14 * math.pi)
    
    def test_str_perim(self):
        res = perimeter("10")
        self.assertEqual(res, 20 * math.pi)

def area(r):
    '''Get radius (r) as float, return area (math.pi * r * r) as float'''
    return math.pi * r * r


def perimeter(r):
    '''Get radius (r) as float, return perimeter (2 * math.pi * r) as float'''
    return 2 * math.pi * r

