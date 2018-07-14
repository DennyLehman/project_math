
"""
This program finds the smallest positive number
that is evenly divisible by 1 - x
"""

def is_divisible(a,div):
	return a % div == 0

def main(x):
	l = [i for i in range(1,x+1)]
	print(l)
	i = l.pop(0)
	while l:
		i = i * l.pop(0)
		print('value is ',i)


if __name__ == '__main__':
	main(10)