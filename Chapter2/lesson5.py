# -*- coding: utf-8 -*-
# lesson 2.5: work with functions: functool and lambda functions
# principle of the function map:
# first variant
'''
x = input().split()
print(x)
map_obj = map(int, x)
print(map_obj)
n = next(map_obj)
k = next(map_obj)
print(k + n)
'''
# second variant
'''
n, k = map(int, input().split())
print(n + k)
'''
# third variant
'''
n, k = (int(i) for i in input().split())
print(n + k)
'''
# principle of the class filter
# Нахождение четных чисел в списке
# first variant
'''
number_list = (int(i) for i in input().split())

def even(x):
	return x % 2 == 0

evens = filter(even, number_list)
for i in evens:
	print(i)
'''
# second variant
'''
number_list = (int(i) for i in input().split())
evens = list(filter(lambda x: x % 2 == 0, number_list))
print(evens)
'''
import operator
'''
print(operator.add(2, 3)) # 2 + 3
print(operator.mul(3, 2)) # 3 * 2
print(operator.contains([1, 2, 3, 4, 5, 6], 7)) # 7 in [1, 2, 3, 4, 5, 6]

x = [1,2,3] 
f = operator.itemgetter(1) # f(x) == x[1]
print(f(x))

f = operator.attrgetter("sort") # f(x) == x.sort
print(f([]))
'''
import functools
'''
x = int("10101010", base = 2)
print(x)
int_2 = functools.partial(int, base = 2)
x = int_2("10101010")
print(x)
'''
'''
x = [
	("Guido", "van", "Rossum"),
	("Haskell", "Curry"),
	("John", "Backus")
]
sort_by_last = functools.partial(list.sort, key = operator.itemgetter(-1))
print(x)
sort_by_last(x)
print(x)
''' 
'''
def mod_checker(x, mod = 0): return lambda y: y % x == mod
mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True
'''