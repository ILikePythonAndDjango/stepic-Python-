# -*- coding: utf-8 -*
# Chapter second: Standart Python tools
# lesson 2.1: Errors and exceptions
'''
x = [1, 2, 3]
print(x[4])
'''
'''
Traceback (most recent call last):
  File "lesson1.py", line 6, in <module>
    print(x[4])
IndexError: list index out of range
'''
'''
def f():
	x = [1, 2, 3]
	print(x[4])
f()
'''
'''
Traceback (most recent call last):
  File "lesson1.py", line 18, in <module>
    f()
  File "lesson1.py", line 17, in f
    print(x[4])
IndexError: list index out of range
'''

# Exception Handling
# Instance1:
'''
try:
	x = [1, 3, 'hello', 7]
	x.sort()
	print(x)
except TypeError:
	print("Type error :(")
print("I can catch")
'''
# Instance2:
'''
def f(x, y):
	try:
		return x / y
	except (TypeError, ZeroDivisionError) as e:
		print(type(e))
		print(e)
		print(e.args)
print(f(5,0))
print(f(5,[]))
'''

# else and finally
'''
def foo(x, y):
	try:
		result = x/y
	except ZeroDivisionError:
		print("Can not be divided into zero!")
	else:
		print("Result is", result, "!")
	finally:
		print("Finally!")
foo(2,1)
foo(2,0)
foo(2,list())
'''

# Inheritance of classes exceptions
'''
Цель здачи: написать программу, которая будет проверят 
наследуемость классов исключений.
Примечание: 
1. Если во множетсве блоков except один класс наследуеться от другого, 
то блок с дочерним классом проверяться не будет.
2. Последовательность можно представить ввиде стека.
Input:
На вход подается число, которое обозначает количество строк
ввода пар классов. Множественного наследования в исключениях нет, т.е.
нет смысла создавать массив.
Затем вводяться значения. На выходе получаем словарь, который показывает
наследственность исключений.
Затем в вводе нужно поместить число, которое будет означать количество 
строк, значения которых означают класс ошибок, которые переданны в блок except.
Output: 
Нужно вывести в консоль те классы ошибок, которые никогда проверяться не будут.
'''
'''
exc = {}
array = []

def is_instance(parent, children, classes):
	if parent in classes[children] or parent == children:
		return True
	else:
		for i in classes[children]:
			if i == "Exception": 
				return False
			else:
				if is_instance(parent, i, classes):
					return True

def get_unuseful_except(arr, dic):
	now_exc_list = []
	unuseful_except = []
	for i in arr:
		if i in now_exc_list:
			unuseful_except.append(i)
			break
		for e in now_exc_list:
			if is_instance(e, i, dic):
				unuseful_except.append(i)
				break
		now_exc_list.append(i)
	return unuseful_except

n = int(input())

for i in range(n):
	put = input()
	if ":" in put:
		child, parent = put.split(" : ")
		exc[child] = parent.split()
	else:
		exc[put] = ["Exception",]

n = int(input())

for i in range(n):
	array.append(input())

for i in get_unuseful_except(array, exc):
	print(i)
'''

# Instance raise structure.
'''
def greet(name):
	if name[0].isupper():
		return "Hello, " + name
	else:
		raise ValueError(name + "ia inapproriate name")

print(greet("Anton"))
print(greet("anton"))
'''
