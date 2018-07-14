
from math import sqrt
import time

def is_prime(x):
	y = int(sqrt(x))+1
	a = 2
	while a < y :
		if x % a == 0:
			#print(x, ' is not prime')
			return False
		a += 1

	#print(x, ' is prime')
	return True

def main(a):
	count = 1
	for x in range(3,1000000,2):
		#print(x)
		if is_prime(x):
			count += 1
		if count == a:
			print(a,' prime reached...\nThe value of the ',a,' prime is ',x)
			return

	print(count, ' numbers were prime')
	
if __name__ == '__main__':
	start = time.time()
	print('This program returns the nth prime number.\nProgram starting now...')
	main(10001)
	print('time to run: ', time.time() - start)