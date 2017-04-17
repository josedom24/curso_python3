#!/usr/bin/env python
def factorial(numero):
	if(numero == 0 or numero == 1):
		return 1
	else:
		return numero * factorial(numero-1)

if __name__ == '__main__':
	print(factorial(5))