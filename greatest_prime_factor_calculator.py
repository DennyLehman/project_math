# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 22:24:17 2018

@author: slin2
"""
import time

class prime_factor_calculator():
    def __init__(self,_number):
    	print('Constructing class...')
    	self.num = _number
    	self.total_numbers = self.num + 1
    	self.primes = self.get_prime_numbers()
    	self.greatest_prime = 0
    	print('Construction complete')

    def function():
    	pass

    # this method returns an array of prime numbers between 2 and total_numbers
    def get_prime_numbers(self):
    	try:
    		self.total_numbers = int(self.total_numbers)
    	except:
    		print('error occured in function get_prime_numbers...\n', total_numbers, ' was passed as a number')
    		return []
    	primes = []
    	new_list = [x for x in range(2,self.total_numbers)]
    	while new_list:
	    	p = new_list.pop(0)
	    	primes.append(p)
	    	# removes all items that are divisible by p
	    	new_list = [item for item in new_list if item % p != 0]

    	return primes
    		
    def get_greatest_divisible_prime(self):
    	primes = self.primes
    	primes.sort()
    	primes.reverse()
    	while primes:
    		p = primes.pop(0)
    		#print(p, ' was popped. checking if ', self.num, ' is divisible by ',p)
    		if self.num % p == 0:
    			self.greatest_prime = p
    			return self.greatest_prime
    	print('could not find a greatest prime')
    	return self.greatest_prime

    def print_name(self):
        print('hello world')

    def execute(self):
    	self.print_name()
    	self.greatest_prime = self.get_greatest_divisible_prime()
    	print('The greatest prime factor of ', self.num, ' is ', self.greatest_prime)
    	
    
if __name__ == '__main__':
    x = int(input())
    start = time.time()
    pfc = prime_factor_calculator(x)
    
    pfc.execute()
    print('Time for execution was {}'.format(time.time() - start))