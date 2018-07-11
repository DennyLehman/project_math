import math
class pal_finder():
	def __init__(self, _num_digits):
		self.digits = _num_digits
		self.palidromes = []

	def is_palindrome(self, val):
		val = str(val)
		half = math.floor(len(val)/2)
		if val[0:half] == val[half:][::-1]:
			return 1
		else:
			return 0


	def get_palindromes(self):
		a = '9' * self.digits
		a = int(a)**2
		print(a)
		while not self.is_palindrome(a) and a > 0:
			a -= 1
			#if self.is_palindrome(a):
		self.palidromes.append(a)
		b = a
		while self.is_palindrome(b):
			b = b - 110
			self.palidromes.append(b)
			#print(b) 
		print(self.palidromes)

	def print_digits(self):
		print(self.digits)


if __name__ == '__main__':
	pf = pal_finder(2)
	#pf.print_digits()
	#print(pf.is_palindrome(102201))
	pf.get_palindromes()
