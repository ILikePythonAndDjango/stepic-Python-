# -*- coding: utf-8 -*-
# lesson 2.3: Iterators and generators

# Instance
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8]

it = iter(lst)
while True:
	try:
		i = next(it)
		print(i)
	except StopIteration:
		break
		'''
'''
from random import random

class RandomIterator:
	def __init__(self, k):
		self.k = k
		self.i = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.i < self.k:
			self.i += 1
			return int((random() * (10 ** len(str(self.k)))) // 1)
		else:
			raise StopIteration
'''
'''x = RandomIterator(3)
print(next(x)) # next(x) ~ x.__next__()
print(next(x))
print(next(x))
print(next(x))''' 
'''
for x in RandomIterator(10):
	print(x)'''

# Перебор эелементов парами
'''
class DoubleEiementListIterator:
	def __init__(self, lst):
		self.lst = lst
		self.i = 0

	def __next__(self):
		if self.i < len(self.lst):
			self.i += 2
			return self.lst[self.i - 2], self.lst[self.i - 1]
		else:
			raise StopIteration

class MyList(list):
	def __iter__(self):
		return DoubleEiementListIterator(self)

for i in MyList([1, 2, 3, 4]):
	print(i)
'''
'''
def random_generator(k):
	for i in range(k):
		yield random()
		return "No more elements"
gen = random_generator(3)
for i in range(3):
	print(next(gen))
'''

'''
class multifilter:
	def judge_half(pos, neg):
		return pos >= neg

	def judge_any(pos, neg):
		return pos >= 1

	def judge_all(pos, neg):
		return neg == 0

	def __init__(self, iterable, *funcs, judge = judge_any):
		self.iterable = iterable
		self.judge = judge
		self.funcs = funcs

	def __iter__(self):
		for it in self.iterable:
			pos, neg = 0, 0
			for func in self.funcs:
				if func(it):
					pos += 1
				else:
					neg += 1
			if self.judge(pos, neg):
				yield it
'''

def primes():
	'''
	Эта функция находит все простые числа по теореме Вильсона.
	Натуральное число p>1 является простым тогда и только тогда, когда (p-1)!+1 делится на p.
	'''
	a = 1
	while True:
		a += 1
		multiplication = 1
		for number in range(a-1):
			multiplication *= (number + 1)
		if (multiplication + 1) % a == 0:
			yield a
gen = primes()
for i in range(31):
	print(next(gen))