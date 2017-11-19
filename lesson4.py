# -*- coding: utf-8 -*-
# lesson 1.4: Namespaces and scopes

'''
status = True
vowels = ["a", "u", "i", "e", "o"]

def check(word):
	global status
	for vowel in vowels:
		if vowel in word:
			status = True
			return True

	status = False
	return False

print(check("ausi")) # True
print(status) # True
print(check("wwwqqq")) # False
print(status) # False
'''

'''
def f():
	status = True
	vowels = ["a", "u", "i", "e", "o"]

	def check(word):
		global status
		for vowel in vowels:
			if vowel in word:
				status = True
				return True
	
		status = False
		return False
	
	print(check("ausi")) # True
	print(status) # True
	print(check("wwwqqq")) # False
	print(status) # True, bacause status is not global, but status is local f()

f()
print(status) # false, because status is global
'''

'''
def f():
	status = True # local Namespace f()
	vowels = ["a", "u", "i", "e", "o"]
	
	def check(word):
		nonlocal status # local Namespace f()
		for vowel in vowels:
			if vowel in word:
				status = True
				return True
	
		status = False
		return False
	
	print(check("ausi")) # True
	print(status) # True
	print(check("wwwqqq")) # False
	print(status) # False

f()
print(status) # NameError, because staus not be in Main Namespace
'''

# Namespace
# Реализация создания пространства имен и добавлениу в них переменных
# У каждого пространства имен  есть уникальный текстовый индефикатор - его имя
# Вашей программе на вход подаются следующие запросы:
'''
create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
add <namespace> <var> – добавить в пространство <namespace> переменную <var>
get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует
'''

'''
a = 0 # Main namespace
def foo():
	b = 1 # local namespace foo() parent - Main
	def bar():
		a = 2 # local namespace bar() parent - foo()
'''

# Namespace stucture: Main(foo(bar()))

def create(namespace, parent):
	"""Создает простраство имен в пространствах имен"""
	x[namespace] = {'parent' : parent, 'vars' : []}

def add(namespace, var):
	"""Добавляет переменные  в пространство имен"""
	x[namespace]['vars'].append(var)

def get(namespace, var):
	"""Возвращает название пространства имен, в которой находиться данная переменная."""
	if namespace == None:
		return None
	elif var in x[namespace]['vars']:
		return namespace
	else:
		return get(x[namespace]['parent'], var)

n = int(input())

x= {
	'global' : {
	'parent' : None, 
	'vars' : []
	}
}

sample_output = []

for i in range(1, n+1):
	cmd, nmsp, var = input().split()
	if cmd == "create":
		create(nmsp, var)
	if cmd == "add":
		add(nmsp, var)
		#print(ns_var[nmsp])
	if cmd == "get":
		sample_output.append(get(nmsp, var))

for e in sample_output:
	print(e)