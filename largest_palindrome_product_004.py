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

	def make_list_of_palindromes(self):
		print('Making list of large palindromes')
		a = int(('9' * self.digits))**2
		l = [x for x in range(math.floor(a*.9),a) if self.is_palindrome(x)]
		# print(l)
		self.palidromes = l
		return

	def factor_palindrome(self):
		a = int('9' * self.digits)
		p = self.palidromes
		d = {}
		while p:
			b = a
			key = p.pop()
			d[key] = []
			while b > a*.9:
				if  key % b == 0:
					d[key].append(b)
				b -= 1
		return d

	def prune_dict(self):
		d = self.factor_palindrome()
		print('pruning list of ')
		for k in list(d.keys()):
			if len(d[k]) < 2:
				#print(k, 'is removed for empty list')
				del d[k]

		# for k,v in d.keys():
		# 	if not v:
		# 		print(k,v)	
		# 		print(k, ' is removed for empty list')
		# 		del d[k]
		print(d)
			



	def print_digits(self):
		print(self.digits)


if __name__ == '__main__':
	pf = pal_finder(3)
	#pf.print_digits()
	#print(pf.is_palindrome(102201))
	#pf.get_palindromes()
	pf.make_list_of_palindromes()
	#print(pf.factor_palindrome())
	pf.prune_dict()