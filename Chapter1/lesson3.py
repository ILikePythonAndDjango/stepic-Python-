# -*- coding: utf-8 -*-
# lesson 1.3: function and stack

# making function:
#def function(text):
#	print(text)

#def name_function(arg1, arg2):
#	# function body
#	return arg1 + arg2

#x = name_function(23, 32)

#print(id(name_function))
#print(type(name_function))
#print(id(x))
#print(type(x))

# Stack functions

'''
def g():
	print("function g")

def f():
	print("function f")
	g()
	print("function f")

print("I'm outside of any function")
f()
print("I'm outside of any function")
''' 

# Stack list on Python3

'''
x = [1, 2, 3]

x.append(4)
x.append(5)

print(x) # [1, 2, 3, 4, 5]

top = x.pop()
print(top) # 5
print(x) # [1, 2, 3, 4, 5]

top = x.pop()
print(top) # 4
print(x) # [1, 2, 3]
'''

# A task on stepic #1
'''
def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return "I don't know :("
'''

'''
def closest_mod_5(x):
	y = x
	while True:
		if y % 5 == 0 and y >= x:
			break
		else:
			y +=1
	return y

print(closest_mod_5(41))
'''

# Passing function arguments

'''
def printab(a, b):
	print(a)
	print(b)

# Postioning method
printab(10, 20)
# Named method
printab(a = 10, b = 20)
printab(b = 10, a = 10)
# Mixed method
printab(10, b = 20)

array = [10, 20]
printab(*array) # printab(array[0], array[1])

args = {'a': 10, 'b': 20}
printab(**args) # = printab(key1 = args[key1],
				#			key2 = args[key2])
'''

# Set of arguments

'''
def foo(a, b, **kwargs):
	print("positional argument a ", a)
	print("positional argument b ", b)
	print("additional araguments:")
	for key in kwargs:
		print(key, kwargs[key])
	return kwargs

print(foo(1, 2, arg3 = 3, arg4 = 4, arg5 = 5, arg6 = 6, arg7 = 6, arg8 = 7, arg9 = 7))
'''

# Recursive functions

'''
def fib(x):
	if x in [0, 1]: return 1
	else: return fib(x-1) + fib(x-2)

y = fib(5)
print(y) #8
'''

'''
n, k = map(int, input().split())

def C(n, k):
	if n in range(1, 11) and k in range(0, 11):
		if k > n:
			return 0
		elif k == n:
			return 1
		else:
			if k == 1:
				return n
			elif not k == 0:
				return C(n-1, k) + C(n - 1, k - 1)
			else:
				return 0
	else:
		return 0

print(C(n, k))
'''

n, k = map(int, input().split())

def C(n, k):
	if k < n and not k == 0:
		return C(n-1,k) + C(n-1,k-1)
	else:
		return 1

print(C(n, k))