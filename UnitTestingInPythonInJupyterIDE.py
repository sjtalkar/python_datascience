# Unit Testing in Python

# Use parent class unittest.TestCase
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
	
suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)    




from math import pi

def circle_area(r):
    if r < 0:
        raise ValueError("The radius cannot be negative")
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a positive interger or decimal value")
    return pi*r**2

circle_area(3)



import unittest
from math import pi
class TestCircleArea(unittest.TestCase):
    def test_area(self):
        #Test areaas when radius > 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2 )
    
    def test_values(self):
        #Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)	
	def test_types(self):
        #Make sure value errors are raised when necessary
        self.assertRaises(TypeError, circle_area, True)	
		self.assertRaises(TypeError, circle_area, 1+3j)
		self.assertRaises(TypeError, circle_area, "NotAllowed")
		
		
			
		
unittest.main(argv=[''], verbosity=2, exit=False)        
    		