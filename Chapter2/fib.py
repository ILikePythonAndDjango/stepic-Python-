# -*- coding: utf-8 -*-

def fib(k):
	if k in [0, 1]:
		return 1
	else:
		return fib(k - 1) + fib(k - 2)

if __name__ == '__main__':
	print(fib(31))