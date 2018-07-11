import math
class pal_finder():
	def __init__(self, _num_digits):
		self.digits = _num_digits

	def is_palindrome(self, val):
		val = str(val)
		half = math.floor(len(val)/2)
		if val[0:half] == val[half:][::-1]:
			return 1
		else:
			return 0


	def print_digits(self):
		print(self.digits)


if __name__ == '__main__':
	pf = pal_finder(2)
	pf.print_digits()
	print(pf.is_palindrome(102201))
