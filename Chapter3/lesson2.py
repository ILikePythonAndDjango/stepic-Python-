# -*- coding: utf-8 -*-
# lesson 2.2: standart method and function for strings
'''
print("abcadnbc".find("nbc"))
print("abcadnbc".find("nbc", 6))
print('abcadnbc'[1:].find("nbc"))
print(str.find.__doc__)
'''
'''
print("cabcd".index("abc"))
print("cabcd".index("abs"))
print(str.index.__doc__)
'''
'''
s = "The man in black fled across the desert, and the gunsliger followed"
print(s.startswith("The man in black", 0, 20))
print(s.startswith(("The woman", "The dog", "The man in black")))
print(str.startswith.__doc__)
'''
'''
s = "python_file.py"
print(s.endswith(".py", 0, 5))
print(s.endswith((".py", ".jpeg", ".txt", ".exel", ".exe", ".del", ".cpp", ".cs", ".pas")))
print(str.endswith.__doc__)
'''
'''
s = "abacaba"
print(s.count("aba"))
print(str.count.__doc__)
'''
# Правосторонние аналоги выше перечиленных функций.
'''
print("abcadnbc".rfind("nbc"))
print("abcadnbc".rfind("nbc", 6))
print('abcadnbc'[1:].rfind("nbc"))
print(str.rfind.__doc__)
'''
'''
print("cabcdabc".rindex("abc"))
print("cabcd".rindex("abs"))
print(str.rindex.__doc__)
'''
'''
s = "This is string"
print(s.lower())
print(s.lower.__doc__)
print(s.upper())
print(s.upper.__doc__)
'''
'''
s = "1,2,3,4"
print(s)
print(s.replace(",", ", "))
print(s.replace.__doc__)
'''
'''
s = "1 \t\t  2 3 4        	"
print(s.split())
print(s.split.__doc__)
'''
'''
s = "	 1, 2, 3, 4 	"
print(repr(s.rstrip()))
print(s.rstrip.__doc__)
print(repr(s.lstrip()))
print(s.lstrip.__doc__)
print(repr(s.strip()))
print(s.strip.__doc__)
'''
'''
s = "_*--1, 2, 3, 4--*_"
print(repr(s.rstrip("*_")))
print(repr(s.lstrip("*_")))
print(repr(s.strip("*_")))
'''
'''
numbers = map(str, [1, 2, 3, 4, 5, 6])
print(repr(" ".join(numbers)))
print(str.join.__doc__)
'''
# formatting strings
"""
name = input("Please, input your name: ")
surename = input("Please, input your surname: ")
print("{0} it's your name and {1} it's your surename.\nHello {0}!\nHow are you?".format(name, surename))
question = input()
print("You're {question}!".format(question=question))
print("{0} it's your name and {1} it's your surename. You're {question}!".format(name, surename, question=question))
"""
'''
import requests
template = "Response from {0.url} with code {0.status_code}"

res = requests.get("https://docs.python.org/3.5")
print(template.format(res))

res = requests.get("https://docs.python.org/3.5/random")
print(template.format(res))
'''