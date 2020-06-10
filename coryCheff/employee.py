import requests
class Employee:
	raise_by=1.05
	def __init__(self,fname,lname,salary):
		self.fname = fname
		self.lname = lname
		self.salary = salary
	@property
	def email(self):
		return f'{self.fname}.{self.lname}@gmail.com'
	@property
	def fullname(self):
		return f'{self.fname} {self.lname}'
	def monthly_schedule(self,month):
		response=requests.get(f'http://company.com/{self.lname}/{month}')
		if response.ok:
			return response.text
		else:
			return 'Bad response!'