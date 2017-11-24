# -*- coding: utf-8 -*-
# lesson 1.6: Inhertance of classes

# Syntax of inhertance

'''
class D: pass
class E: pass
class B(D, E): pass
class C: pass
class A(B, C): pass

# issubclass(class, class) -- это функция проверяет наследуемость классов

print(issubclass(A, A)) # True
print(issubclass(C, D)) # False
print(issubclass(A, D)) # True
print(issubclass(C, object)) # True
print(issubclass(object, C)) # False

# isinstance() -- это функция проверяет насдеуемость типа объекта и второго класса, объекта.

x = A()

print(isinstance(x, A))
print(isinstance(x, B))
print(isinstance(x, object))
print(isinstance(x, str))
'''

# Instance multiple inheritance classes

'''
class EvenLengthMixin:
	def even_length(self):
		return len(self) % 2 == 0
'''

'''
class MyList(list, EvenLengthMixin):
	pass

class MyDict(dict, EvenLengthMixin):
	pass

class MyTuple(tuple, EvenLengthMixin):
	pass

print(MyList.mro())
# [<class '__main__.MyList'>, <class 'list'>, 
# <class '__main__.EvenLengthMixin'>, <class 'object'>]
x  = MyList([1, 2, 3])
print(x.even_length()) #False
x.append(4)
print(x.even_length()) # True

x = MyTuple()
print(x)

x = MyDict()
x["key"] = 'value'
x["id"] = 324
print(x.even_length()) # True
'''

'''
class MyList(list, EvenLengthMixin):
	def pop(self):
		x = super(MyList, self).pop()
		print("Last value is", x)
		return x

ml = MyList([1, 2, 3, 4, 17])
z = ml.pop() # Last value is 17
print(z) # 17
print(ml) # [1, 2, 4]
'''

# Inheritance modeling

"""""
Задача состоит в том, чтобы смоделировать наследовакие классов.
На взодные данные будут подоваться названия класса дочерниго и
класса родиетля. И нужно проверить: являются они таковыми или нет!

Сначала в первой строке ввода содержиться число классов
В следующих сторах содержаться классы. 
Затем в строке нужно ввести число количества  запросов. 
Для каждого из запросов в отдельной строке выводиться слово "Yes",
если класс1 являеться предком класса2, и "No" если не являеться.
"""

'''
def is_instance(parent, children):
	if parent in classes[children] or parent == children:
		return True
	else:
		for i in classes[children]:
			if i == "object": 
				return False
			else:
				if is_instance(parent, i):
					return True

n = int(input())

classes_n = list()
query_q = list()

for i in range(n):
	classes_n.append(input())

classes = {}

for i in classes_n:
	if ":" in i:
		children, parent = i.split(":")
		classes[children.strip()] = parent.split()
	else:
		classes[i] = ["object", ];

print(classes)

q = int(input())

for i in range(q):
	query_q.append(input())

for i in query_q:
	parent, children = i.split()
	if is_instance(parent, children):
		print("Yes!")
	else:
		print("No!")
'''

# Stack modeling

'''
class ExtendedStack(list):
	def sum(self):
		top1 = super(ExtendedStack, self).pop()
		top2 = super(ExtendedStack, self).pop()
		super(ExtendedStack, self).append(top1 + top2)

	def sub(self):
		top1 = super(ExtendedStack, self).pop()
		top2 = super(ExtendedStack, self).pop()
		super(ExtendedStack, self).append(top1 - top2)

	def mul(self):
		top1 = super(ExtendedStack, self).pop()
		top2 = super(ExtendedStack, self).pop()
		super(ExtendedStack, self).append(top1 * top2)

	def div(self):
		top1 = super(ExtendedStack, self).pop()
		top2 = super(ExtendedStack, self).pop()
		super(ExtendedStack, self).append(top1 // top2)

array = ExtendedStack()
array.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array)
array.sum()
print(array)
array.sub()
print(array)
array.mul()
print(array)
array.div()
print(array)
'''

# Expanding functionality with multiple inheritance

import time

class Loggable:
	def log(self, msg):
		print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
	def append(self, obj):
		self.log(obj)
		super(LoggableList, self).append(obj)

array = LoggableList()

array.append("Hello!")
array.append("How are yoy!")
array.append("Do you like a football?")
print(array)