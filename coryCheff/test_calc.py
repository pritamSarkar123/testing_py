import unittest
import calc

class TestCalc(unittest.TestCase):
	#test_  < this is mandatory for any test method
	def test_addition(self):
		self.assertEqual(calc.addition(10,5),15)
		self.assertEqual(calc.addition(10,-10),0)
		self.assertEqual(calc.addition(-10,-10),-20)
	def test_subtraction(self):
		self.assertEqual(calc.subtraction(10,5),5)
		self.assertEqual(calc.subtraction(10,-10),20)
		self.assertEqual(calc.subtraction(-10,-10),0)

	def test_multiplication(self):
		self.assertEqual(calc.multiplication(10,5),50)
		self.assertEqual(calc.multiplication(10,-10),-100)
		self.assertEqual(calc.multiplication(-10,-10),100)
	def test_division(self):
		self.assertEqual(calc.division(10,5),2)
		self.assertEqual(calc.division(10,-10),-1)
		self.assertEqual(calc.division(-10,-10),1)
		self.assertEqual(calc.division(10,0),0.0)
		#if we dont use the decorator on division 
		#self.asertRaises(ValueError,calc.division,10,0)
		#OR
		#we have to use context manager
		#with self.assertRaises(ValueError): <-context manager
		#	calc.division(10,0)

#if main block not present the we have to do 
#python -m unittest test_calc.py
if __name__ =="__main__":
	unittest.main()