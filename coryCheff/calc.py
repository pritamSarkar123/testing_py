
def outer(func_name):
	def inner(a,b):
		if b==0:
			a,b=b,a
		return func_name(a,b)
	return inner

def addition(a,b):
	return a + b
def multiplication(a,b):
	return a * b
def subtraction(a,b):
	return a - b
@outer
def division(a,b):
	return a / b