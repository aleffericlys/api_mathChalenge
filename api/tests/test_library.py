import unittest
from api.src.library import Numbers, Number  # Importando as classes que serão testadas

class TestNumberMethods(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(Number.sum(5, 10), 15)
        self.assertEqual(Number.sum(-5, 10), 5)
        self.assertEqual(Number.sum(0, 0), 0)
        
    def test_divide(self):
        self.assertEqual(Number.divide(10, 2), 5.0)
        self.assertEqual(Number.divide(7, 2), 3.5)
        self.assertRaises(ZeroDivisionError, Number.divide, 10, 0)

class TestNumbersMethods(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(Numbers.sum([1, 2, 3, 4]), 10)
        self.assertEqual(Numbers.sum([0, 0, 0]), 0)
        self.assertEqual(Numbers.sum([-1, -2, -3]), -6)
    
    def test_average(self):
        self.assertEqual(Numbers.average([1, 2, 3, 4]), 2.5)
        self.assertEqual(Numbers.average([0, 0, 0]), 0.0)
        self.assertEqual(Numbers.average([10, 20, 30]), 20.0)

if __name__ == '__main__':
    unittest.main()
