import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):
	#ONE TIME ONLY
	# @classmethod                  #<----------only once before all testing
	# def setUpClass(cls):
	# 	print('setUpClass')
	# 	cls.emp_1=Employee("Pritam","Sarkar",60000)
	# 	cls.emp_2=Employee("Eshani","Jas",70000)
	# 	cls.emp_3=Employee("Rahul","Banerjee",60000)
	# 	cls.emp_4=Employee("Rishika","Kundu",70000)

	# @classmethod
	# def tearDownClass(cls):       #<-----------onely once after all testing
	# 	print('tearDownClass')

	#FOR ALL TESTS
	def setUp(self):               #<----------before each testing
		print('setUp')
		self.emp_1=Employee("Pritam","Sarkar",60000)
		self.emp_2=Employee("Eshani","Jas",70000)
		self.emp_3=Employee("Rahul","Banerjee",60000)
		self.emp_4=Employee("Rishika","Kundu",70000)


	def tearDown(self):            #<-----------after each testing
		print('tearDown')


	def test_fullname(self):
		print('test_fullname')
		self.assertEqual(self.emp_1.fullname,"Pritam Sarkar")
		self.assertEqual(self.emp_2.fullname,"Eshani Jas")
		self.assertEqual(self.emp_3.fullname,"Rahul Banerjee")
		self.assertEqual(self.emp_4.fullname,"Rishika Kundu")

		self.emp_1.fname = "Pritam_"
		self.emp_2.fname = "Eshani_"
		self.emp_3.fname ="Rahul_"
		self.emp_4.fname = "Rishika_"

		self.assertEqual(self.emp_1.fullname,"Pritam_ Sarkar")
		self.assertEqual(self.emp_2.fullname,"Eshani_ Jas")
		self.assertEqual(self.emp_3.fullname,"Rahul_ Banerjee")
		self.assertEqual(self.emp_4.fullname,"Rishika_ Kundu")

	def test_email(self):
		print('test_email')
		self.assertEqual(self.emp_1.email,"Pritam.Sarkar@gmail.com")
		self.assertEqual(self.emp_2.email,"Eshani.Jas@gmail.com")
		self.assertEqual(self.emp_3.email,"Rahul.Banerjee@gmail.com")
		self.assertEqual(self.emp_4.email,"Rishika.Kundu@gmail.com")

		self.emp_1.fname = "Pritam_"
		self.emp_2.fname = "Eshani_"
		self.emp_3.fname ="Rahul_"
		self.emp_4.fname = "Rishika_"

		self.assertEqual(self.emp_1.email,"Pritam_.Sarkar@gmail.com")
		self.assertEqual(self.emp_2.email,"Eshani_.Jas@gmail.com")
		self.assertEqual(self.emp_3.email,"Rahul_.Banerjee@gmail.com")
		self.assertEqual(self.emp_4.email,"Rishika_.Kundu@gmail.com")

	def test_monthly_schedule(self):
		with patch('employee.requests.get') as mocked_get:   #mocked_get is a mock apis get end point
			mocked_get.return_value.ok=True	                 #setting what to return 
			mocked_get.return_value.text='Success'
			schedule=self.emp_1.monthly_schedule('May')       #request using url
			mocked_get.assert_called_with('http://company.com/Sarkar/May') #checks requested url with the stated url
			self.assertEqual(schedule,'Success')

			mocked_get.return_value.ok=False
			schedule=self.emp_2.monthly_schedule('May')
			mocked_get.assert_called_with('http://company.com/Jas/May')
			self.assertEqual(schedule,'Bad response!')



if __name__ == '__main__':
	unittest.main()
